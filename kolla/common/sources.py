# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

SOURCES = {
    'openstack-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/requirements/'
                     'requirements-${openstack_branch}.tar.gz')},
    'aodh-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/aodh/'
                     'aodh-${openstack_branch}.tar.gz')},
    'barbican-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/barbican/'
                     'barbican-${openstack_branch}.tar.gz')},
    'bifrost-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/bifrost/'
                     'bifrost-${openstack_branch}.tar.gz')},
    'blazar-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/blazar/'
                     'blazar-${openstack_branch}.tar.gz')},
    'ceilometer-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ceilometer/'
                     'ceilometer-${openstack_branch}.tar.gz')},
    'cinder-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/cinder/'
                     'cinder-${openstack_branch}.tar.gz')},
    'cloudkitty-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/cloudkitty/'
                     'cloudkitty-${openstack_branch}.tar.gz')},
    'cyborg-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/cyborg/'
                     'cyborg-${openstack_branch}.tar.gz')},
    'designate-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/designate/'
                     'designate-${openstack_branch}.tar.gz')},
    'etcd': {
        # NOTE(wszumski): Upgrade one minor version at a time:
        # https://etcd.io/docs/v3.4/upgrades/upgrade_3_4/
        'version': '3.5.21',
        'type': 'url',
        'sha256': {
            'amd64': 'adddda4b06718e68671ffabff2f8cee48488ba61ad82900e639d108f2148501c',  # noqa: E501
            'arm64': '95bf6918623a097c0385b96f139d90248614485e781ec9bee4768dbb6c79c53f'},  # noqa: E501
        'location': ('https://github.com/etcd-io/etcd/'
                     'releases/download/v${version}'
                     '/etcd-v${version}-linux-${debian_arch}.tar.gz')},
    'glance-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/glance/'
                     'glance-${openstack_branch}.tar.gz')},
    'gnocchi-base': {
        'type': 'git',
        'reference': '4.6.4',
        'location': ('https://github.com/gnocchixyz/'
                     'gnocchi.git')},
    'heat-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/heat/'
                     'heat-${openstack_branch}.tar.gz')},
    'horizon': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/horizon/'
                     'horizon-${openstack_branch}.tar.gz')},
    'horizon-plugin-blazar-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/blazar-dashboard/'
                     'blazar-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-cloudkitty-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/cloudkitty-dashboard/'
                     'cloudkitty-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-designate-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/designate-dashboard/'
                     'designate-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-fwaas-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-fwaas-dashboard/'
                     'neutron-fwaas-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-heat-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/heat-dashboard/'
                     'heat-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-ironic-ui': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ironic-ui/'
                     'ironic-ui-${openstack_branch}.tar.gz')},
    'horizon-plugin-magnum-ui': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/magnum-ui/'
                     'magnum-ui-${openstack_branch}.tar.gz')},
    'horizon-plugin-manila-ui': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/manila-ui/'
                     'manila-ui-${openstack_branch}.tar.gz')},
    'horizon-plugin-masakari-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/masakari-dashboard/'
                     'masakari-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-mistral-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/mistral-dashboard/'
                     'mistral-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-neutron-vpnaas-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-vpnaas-dashboard/'
                     'neutron-vpnaas-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-octavia-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/octavia-dashboard/'
                     'octavia-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-tacker-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/tacker-horizon/'
                     'tacker-horizon-${openstack_branch}.tar.gz')},
    'horizon-plugin-trove-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/trove-dashboard/'
                     'trove-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-venus-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/venus-dashboard/'
                     'venus-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-watcher-dashboard': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/watcher-dashboard/'
                     'watcher-dashboard-${openstack_branch}.tar.gz')},
    'horizon-plugin-zun-ui': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/zun-ui/'
                     'zun-ui-${openstack_branch}.tar.gz')},
    'ironic-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ironic/'
                     'ironic-${openstack_branch}.tar.gz')},
    'ironic-inspector': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ironic-inspector/'
                     'ironic-inspector-${openstack_branch}.tar.gz')},
    'ironic-conductor-plugin-prometheus-exporter': {
        'type': 'url',
        'location': (
            '$tarballs_base/openstack/ironic-prometheus-exporter/'
            'ironic-prometheus-exporter-${openstack_branch}.tar.gz')},
    'keystone-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/keystone/'
                     'keystone-${openstack_branch}.tar.gz')},
    'kuryr-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/kuryr/'
                     'kuryr-${openstack_branch}.tar.gz')},
    'kuryr-libnetwork': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/kuryr-libnetwork/'
                     'kuryr-libnetwork-${openstack_branch}.tar.gz')},
    'letsencrypt-lego': {
        'version': 'v4.23.1',
        'type': 'url',
        'sha256': {
            'amd64': '1fd60b1fd59c239bed22719a5de402cb745d1f933540cb1ec196e2c03e6e8882',  # noqa: E501
            'arm64': '1114745108343286d4bff189b4bdee3cba9d07ebcacc673860d91ab951d31e0d'},  # noqa: E501
        'location': ('https://github.com/go-acme/lego/'
                     'releases/download/${version}/'
                     'lego_${version}_linux_${debian_arch}.tar.gz')},
    'magnum-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/magnum/'
                     'magnum-${openstack_branch}.tar.gz')},
    'magnum-conductor-plugin-helm': {
        'version': 'v3.18.2',
        'type': 'url',
        'sha256': {
            'amd64': 'c5deada86fe609deefdf40e9cbbe3da2f8cf3f6a4551a0ebe7886dc8fcf98bce',  # noqa: E501
            'arm64': '03181a494a0916b370a100a5b2536104963b095be53fb23d1e29b2afb1c7de8d'},  # noqa: E501
        'location': ('https://get.helm.sh/helm'
                     '-${version}-linux-${debian_arch}.tar.gz')},
    'manila-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/manila/'
                     'manila-${openstack_branch}.tar.gz')},
    'masakari-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/masakari/'
                     'masakari-${openstack_branch}.tar.gz')},
    'masakari-monitors': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/masakari-monitors/'
                     'masakari-monitors-${openstack_branch}.tar.gz')},
    'mistral-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/mistral/'
                     'mistral-${openstack_branch}.tar.gz')},
    'mistral-base-plugin-tacker': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/tacker/'
                     'tacker-${openstack_branch}.tar.gz')},
    'neutron-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron/'
                     'neutron-${openstack_branch}.tar.gz')},
    'neutron-base-plugin-neutron-fwaas': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-fwaas/'
                     'neutron-fwaas-${openstack_branch}.tar.gz')},
    'neutron-base-plugin-networking-baremetal': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/networking-baremetal/'
                     'networking-baremetal-${openstack_branch}.tar.gz')},
    'neutron-base-plugin-networking-generic-switch': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/networking-generic-switch/'
                     'networking-generic-switch-${openstack_branch}.tar.gz')},
    'neutron-base-plugin-networking-sfc': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/networking-sfc/'
                     'networking-sfc-${openstack_branch}.tar.gz')},
    'neutron-base-plugin-vpnaas-agent': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-vpnaas/'
                     'neutron-vpnaas-${openstack_branch}.tar.gz')},
    'neutron-bgp-dragent': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-dynamic-routing/'
                     'neutron-dynamic-routing-${openstack_branch}.tar.gz')},
    'neutron-server-plugin-neutron-dynamic-routing': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-dynamic-routing/'
                     'neutron-dynamic-routing-${openstack_branch}.tar.gz')},
    'neutron-vpnaas-agent': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/neutron-vpnaas/'
                     'neutron-vpnaas-${openstack_branch}.tar.gz')},
    'nova-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/nova/'
                     'nova-${openstack_branch}.tar.gz')},
    'nova-base-plugin-blazar': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/blazar-nova/'
                     'blazar-nova-${openstack_branch}.tar.gz')},
    'octavia-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/octavia/'
                     'octavia-${openstack_branch}.tar.gz')},
    'octavia-api-plugin-ovn-octavia-provider': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ovn-octavia-provider/'
                     'ovn-octavia-provider-${openstack_branch}.tar.gz')},
    'octavia-driver-agent-plugin-ovn-octavia-provider': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/ovn-octavia-provider/'
                     'ovn-octavia-provider-${openstack_branch}.tar.gz')},
    'placement-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/placement/'
                     'placement-${openstack_branch}.tar.gz')},
    'prometheus-alertmanager': {
        'version': '0.28.1',
        'type': 'url',
        'sha256': {
            'amd64': '5ac7ab5e4b8ee5ce4d8fb0988f9cb275efcc3f181b4b408179fafee121693311',  # noqa: E501
            'arm64': 'd8832540e5b9f613d2fd759e31d603173b9c61cc7bb5e3bc7ae2f12038b1ce4f'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/alertmanager/'
                     'releases/download/v${version}/'
                     'alertmanager'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-blackbox-exporter': {
        'version': '0.26.0',
        'type': 'url',
        'sha256': {
            'amd64': '4b1bb299c685ecff75d41e55e90aae8e02a658395fb14092c7f9c5c9d75016c7',  # noqa: E501
            'arm64': 'afb5581b1d4ea45078eebc96e4f989f912d1144d2cc131db8a6c0963bcc6a654'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/blackbox_exporter/'
                     'releases/download/v${version}/'
                     'blackbox_exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-cadvisor': {
        'version': '0.52.1',
        'type': 'url',
        'sha256': {
            'amd64': '37b04a2c2e939966ff8ea17628afda5f3a24ca647be36b3ba3748ed016a15ecc',  # noqa: E501
            'arm64': '56ad56304b2829747b455d1f6e7afc1dd6c0db415bb302c584f5b6079b195dda'},  # noqa: E501
        'location': ('https://github.com/'
                     'google/cadvisor/'
                     'releases/download/v${version}/'
                     'cadvisor'
                     '-v${version}-linux-${debian_arch}')},
    'prometheus-elasticsearch-exporter': {
        'version': '1.9.0',
        'type': 'url',
        'sha256': {
            'amd64': '472fcafab63c5a3a2dd17d9a5e9919de4741a72e4f286c1e6252f3d99cebe425',  # noqa: E501
            'arm64': 'd1ba36fe0a6b7ce84d995e728044b53cc869f6033ce0ead4601232205d850947'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus-community/elasticsearch_exporter/'
                     'releases/download/v${version}/'
                     'elasticsearch_exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-libvirt-exporter': {
        'version': '1.7.2',
        'type': 'url',
        'sha256': {
            'amd64': '5226fb0dfeee4e979b19db619a78141530cd8a4e868a3d9136010f2de420aca1',  # noqa: E501
            'arm64': '35b3220facd6cc672216ab05df808f67cab58184d9908ebd641e22f185c2fbc9'},  # noqa: E501
        'location': ('https://github.com/'
                     'inovex/prometheus-libvirt-exporter/'
                     'releases/download/v${version}/'
                     'prometheus-libvirt-exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-memcached-exporter': {
        'version': '0.15.3',
        'type': 'url',
        'sha256': {
            'amd64': '7e4eb9f4af3971918fbfd35fa31b74dc08b2a728f488f934d8c7c7ecced2c85f',  # noqa: E501
            'arm64': '8565c24a80e30e189479b1092d23a7cc9173fc3f3591881b34ed99c62c3ead6f'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/memcached_exporter/'
                     'releases/download/v${version}/'
                     'memcached_exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-mtail': {
        'version': '3.0.8',
        'type': 'url',
        'sha256': {
            'amd64': '123c2ee5f48c3eff12ebccee38befd2233d715da736000ccde49e3d5607724e4',  # noqa: E501
            'arm64': 'aa04811c0929b6754408676de520e050c45dddeb3401881888a092c9aea89cae'},  # noqa: E501
        'location': ('https://github.com/'
                     'google/mtail/'
                     'releases/download/v${version}/'
                     'mtail'
                     '_${version}_linux_${debian_arch}.tar.gz')},
    'prometheus-mysqld-exporter': {
        'version': '0.16.0',
        'type': 'url',
        'sha256': {
            'amd64': '32fe0b59ef3f52624a1958aaf6b8855f27c2b492a7026d62a975bbd251be209d',  # noqa: E501
            'arm64': '9ffc6e107bd122e68a95fa5c194bc3fc257104fef6ed720a26a240cd608c777b'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/mysqld_exporter/'
                     'releases/download/v${version}/'
                     'mysqld_exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-node-exporter': {
        'version': '1.9.1',
        'type': 'url',
        'sha256': {
            'amd64': 'becb950ee80daa8ae7331d77966d94a611af79ad0d3307380907e0ec08f5b4e8',  # noqa: E501
            'arm64': '848f139986f63232ced83babe3cad1679efdbb26c694737edc1f4fbd27b96203'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/node_exporter/'
                     'releases/download/v${version}/'
                     'node_exporter'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'prometheus-openstack-exporter': {
        'version': '1.7.0',
        'type': 'url',
        'sha256': {
            'amd64': 'dfaa0d3dcff22e882d3f61c56bb9ac6f70790df9d67361464159bbb4c7223192',  # noqa: E501
            'arm64': 'd6e0b23fe755732a93796255e3a2be8ec5a699b0a64c21afd377c60ccf60cd55'},  # noqa: E501
        'location': ('https://github.com/'
                     'openstack-exporter/openstack-exporter/'
                     'releases/download/v${version}/'
                     'openstack-exporter'
                     '_${version}_linux_${debian_arch}.tar.gz')},
    'prometheus-ovn-exporter': {
        'version': '1.0.7',
        'type': 'url',
        'sha256': {
            'amd64': '38d9874ddca1581574a7fa0a28ea53447a57dada37bb1385adeb766e6e819de0',  # noqa: E501
            'arm64': 'e03f6a5ab4cf2855a498697026981273ce3c9ff16bd9bb6c97fd7f1344ec2067'},  # noqa: E501
        'location': ('https://github.com/'
                     'greenpau/ovn_exporter/'
                     'releases/download/v${version}/'
                     'ovn-exporter'
                     '_${version}_linux_${debian_arch}.tar.gz')},
    'prometheus-server': {
        'version': '3.4.1',
        'type': 'url',
        'sha256': {
            'amd64': '09203151c132f36b004615de1a3dea22117ad17e6d7a59962e34f3abf328f312',  # noqa: E501
            'arm64': '2a85be1dff46238c0d799674e856c8629c8526168dd26c3de2cecfbfc6f9a0a2'},  # noqa: E501
        'location': ('https://github.com/'
                     'prometheus/prometheus/'
                     'releases/download/v${version}/'
                     'prometheus'
                     '-${version}.linux-${debian_arch}.tar.gz')},
    'skyline-apiserver': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/skyline-apiserver/'
                     'skyline-apiserver-${openstack_branch}.tar.gz')},
    'skyline-console': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/skyline-console/'
                     'skyline-console-${openstack_branch}.tar.gz')},
    'tacker-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/tacker/'
                     'tacker-${openstack_branch}.tar.gz')},
    'tacker-base-plugin-networking-sfc': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/networking-sfc/'
                     'networking-sfc-${openstack_branch}.tar.gz')},
    'trove-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/trove/'
                     'trove-${openstack_branch}.tar.gz')},
    'venus-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/venus/'
                     'venus-${openstack_branch}.tar.gz')},
    'watcher-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/watcher/'
                     'watcher-${openstack_branch}.tar.gz')},
    'zun-base': {
        'type': 'url',
        'location': ('$tarballs_base/openstack/zun/'
                     'zun-${openstack_branch}.tar.gz')}
}
