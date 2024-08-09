#!/usr/bin/env python3
# coding: utf-8
# Copyright 2023 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===========================================================================
import os
import glob
import re
import shutil

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common_utils import clean_env


class Check(object):
    max_k8s_version = '1.26'

    def __init__(self):
        self.module = AnsibleModule(argument_spec=dict(
            tags=dict(type='list'),
            master_groups=dict(type='list'),
            worker_groups=dict(type='list'),
            current_hostname=dict(type='str'),
            kube_vip=dict(type='str'),
            k8s_api_server_ip=dict(type='str'),
            kube_interface=dict(type='str'),
            use_k8s_version=dict(type='str')

        ))
        self.tags = self.module.params['tags']
        self.master_groups = self.module.params['master_groups']
        self.worker_groups = self.module.params['worker_groups']
        self.current_hostname = self.module.params['current_hostname']
        self.kube_vip = self.module.params['kube_vip']
        self.k8s_api_server_ip = self.module.params['k8s_api_server_ip']
        self.kube_interface = self.module.params['kube_interface']
        self.use_k8s_version = self.module.params['use_k8s_version']
        self.facts = dict()
        self.kubeadm_version = ''
        self.kubectl_version = ''
        self.kubelet_version = ''
        self.facts['use_old_k8s_version'] = old = 'mef' in self.tags or self.use_k8s_version != '1.25.3'
        self.facts.update({
            'pull_cmd': 'docker pull' if old else 'nerdctl -n k8s.io pull --insecure-registry',
            'import_cmd': 'docker load -i' if old else 'nerdctl -n k8s.io load --all-platforms -i'
        })

    def check_k8s_version(self):
        kubeadm_bin = self.module.get_bin_path('kubeadm')
        if kubeadm_bin:
            _, out, _ = self.module.run_command('kubeadm version', check_rc=True)
            reg = re.search(r'GitVersion:\"v(.+?)\"', out)
            if reg:
                self.kubeadm_version = reg.group(1)
        kubectl_bin = self.module.get_bin_path('kubectl')
        if kubectl_bin:
            _, out, _ = self.module.run_command('kubectl version')
            reg = re.search(r'GitVersion:\"v(.+?)\"', out)
            if reg:
                self.kubectl_version = reg.group(1)
        kubelet_bin = self.module.get_bin_path('kubelet')
        if kubelet_bin:
            _, out, _ = self.module.run_command('kubelet --version', check_rc=True)
            self.kubelet_version = out.strip().split()[-1].strip('v')
        self.facts['k8s_installed'] = bool(self.kubeadm_version or self.kubectl_version or self.kubelet_version)
        if self.kubeadm_version != self.kubectl_version or self.kubeadm_version != self.kubelet_version:
            msg = 'k8s on this node has different version, kubeadm_version: {}, kubectl_version: {},' \
                  'kubelet_version: {}'.format(self.kubeadm_version, self.kubectl_version, self.kubelet_version)
            self.module.fail_json(msg)
        if self.kubelet_version > self.max_k8s_version:
            self.module.fail_json(msg='node k8s version should be <= {}'.format(self.max_k8s_version))

    def check_k8s(self):
        if not self.kubectl_version:
            self.facts['k8s_initialized'] = False
            return
        _, out, _ = self.module.run_command('kubectl get node -o wide')
        host = self.k8s_api_server_ip or self.current_hostname
        self.facts['k8s_initialized'] = host in out
        _, out, _ = self.module.run_command('kubectl cluster-info')
        result = re.search(r'://(.+?):', out)
        if not result:
            return
        control_host = result.group(1)
        if control_host not in self.master_groups + [self.kube_vip]:
            msg = "node join another k8s cluster({}), if you want to join this k8s cluster, please execute command " \
                  "'kubeadm reset -f && rm -rf $HOME/.kube /etc/cni/net.d' manually on node".format(control_host)
            self.module.log(msg)
            self.module.fail_json(msg=msg)
        flag = len(self.master_groups) > 1 and self.current_hostname in self.master_groups and self.kube_vip and \
            self.kube_interface
        if not self.facts['k8s_initialized']:
            self.module.run_command('kubectl reset -f')
            for path in [os.path.expanduser('~/.kube'), '/etc/cni/net.d ']:
                if os.path.exists(path):
                    shutil.rmtree(path)
            if flag:
                self.module.run_command('ip addr delete {} dev {}'.format(self.kube_vip, self.kube_interface))

    def check_driver_status(self):
        if self.current_hostname not in self.worker_groups or 'mef' in self.tags:
            return
        if not self.module.get_bin_path('npu-smi'):
            self.module.fail_json(msg='please check that this node has the driver installed.')
        rc, out, err = self.module.run_command('lspci')
        if rc or err:
            self.module.fail_json(msg='can lspci failed: {}'.format(err))
        if not ('processing_accelerator' in out and 'Device d801' in out):
            return
        devices = glob.glob('/dev/davinci[0-9]*')
        if not devices:
            self.module.warn('no davinci device')
        if not self.module.get_bin_path('hccn_tool'):
            return
        for device in devices:
            device_id = device.replace('/dev/davinci', '')
            cmd = 'hccn_tool -i {} -ip -g'.format(device_id)
            rc, out, err = self.module.run_command(cmd)
            if rc or err:
                self.module.fail_json(msg='run cmd failed: {}'.format(err))
            if 'ipaddr' not in out:
                self.module.warn('{} has no device IP'.format(device_id))

    def run(self):
        clean_env()
        if self.current_hostname in self.master_groups + self.worker_groups:
            self.check_k8s_version()
            self.check_k8s()
        self.check_driver_status()
        self.module.exit_json(msg='check ok', ansible_facts=self.facts)


if __name__ == '__main__':
    Check().run()
