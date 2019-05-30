from translator.common.requirement import ProviderRequirement
from translator.common.exception import UnavailableNodeFilterError
from toscaparser.common.exception import ExceptionCollector


class OpenstackSecurityGroupRequirement(ProviderRequirement):

    NAME = 'security_group'

    def __init__(self, data):
        super(OpenstackSecurityGroupRequirement, self).__init__(data)

        self.name = self.data.get('node_filter', {}).get('properties', {}).get('name')
        if not self.name:
            ExceptionCollector.appendException(UnavailableNodeFilterError(
                what=self.NAME,
                param='name'
            ))
