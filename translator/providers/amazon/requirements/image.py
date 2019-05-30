from translator.providers.amazon.nodefilters.image import AmazonImageNodeFilter
from translator.common.requirement import ProviderRequirement


class AmazonImageRequirement(ProviderRequirement):

    NAME = 'image'
    NODE_FILTER = AmazonImageNodeFilter

    def __init__(self, data):
        super(AmazonImageRequirement, self).__init__(data)
        self.filter()
