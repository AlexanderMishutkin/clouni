from toscatranslator.providers.common.all_requirements import ProviderRequirements


class OpenstackRequirements (ProviderRequirements):

    REQUIREMENT_KEY_BY_NAME = dict(
        boot_volume='volume',
        flavor='flavor',
        image='image',
        interfaces='subnet',
        network='network',
        network_name='network',
        nics=('network', 'port'),
        security_group='security_group',
        security_groups='security_group',
        server='server',
        snapshot_id='volume',
        volumes='volume'
    )

    PROVIDER = 'openstack'

    def requirement_key_by_name(self, name):
        return self.REQUIREMENT_KEY_BY_NAME.get(name)

    def nodefilter_key_by_key(self, key):
        return key

    def provider(self):
        return self.PROVIDER
