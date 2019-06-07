##########################################################################
# FACTS_BY_PROVIDER
##########################################################################

amazon_facts = dict(
    ec2_eni_facts=['network_interfaces'],
    ec2_ami_facts=['images'],
    ec2_vpc_facts=['vpcs'],
    ec2_subnet_facts=['subnets'],
    ec2_instance_type_facts=['ansible_facts', 'amazon_instance_types']
)

openstack_facts = dict(
    openstack_flavor_facts=['ansible_facts', 'openstack_flavors'],
    openstack_image_facts=['ansible_facts', 'openstack_image'],
    openstack_network_facts=['ansible_facts', 'openstack_networks'],
    openstack_port_facts=['ansible_facts', 'openstack_ports'],
    openstack_server_facts=['ansible_facts', 'openstack_servers'],
    openstack_subnet_facts=['ansible_facts', 'openstack_subnets']
)

FACTS_BY_PROVIDER = dict(
    amazon=amazon_facts,
    openstack=openstack_facts
)

##########################################################################
# FACT_NAME_BY_NODE_NAME
##########################################################################

amazon_fact_name_by_node_name = dict(
    ElasticNetworkInterface='ec2_eni_facts',
    Image='ec2_ami_facts',
    VirtualPrivateCloud='ec2_vpc_facts',
    VirtualPrivateCloudSubnet='ec2_subnet_facts'
)

openstack_fact_name_by_node_name = dict(
    flavor='openstack_flavor_facts',
    image='openstack_image_facts',
    network='openstack_network_facts',
    port='openstack_port_facts',
    server='openstack_server_facts',
    subnet='openstack_subnet_facts'
)

FACT_NAME_BY_NODE_NAME = dict(
    amazon=amazon_fact_name_by_node_name,
    openstack=openstack_fact_name_by_node_name
)

##########################################################################
# PROVIDER_NODEFILTER_FACTS_BY_KEY
##########################################################################

openstack_facts_by_nodefilter_key = dict(
    flavor='openstack_flavor_facts',
    image='openstack_image_facts',
    network='openstack_network_facts',
    port='openstack_port_facts',
    server='openstack_server_facts',
    subnet='openstack_subnet_facts'
)

PROVIDER_NODEFILTER_FACTS_BY_KEY = dict(
    openstack=openstack_facts_by_nodefilter_key
)

##########################################################################
# FACTS REFACTORING
##########################################################################
refactoring_flavor_keys = dict(

)
refactoring_image_keys = dict(

)
refactoring_network_keys = dict(

)
refactoring_port_keys = dict(

)
refactoring_server_keys = dict(

)
refactoring_subnet_keys = dict(

)

REFACTORING_FACT_KEYS = dict(
    ec2_eni_facts=None,
    ec2_ami_facts=None,
    ec2_vpc_facts=None,
    ec2_subnet_facts=None,
    ec2_instance_type_facts=None,

    openstack_flavor_facts=refactoring_flavor_keys,
    openstack_image_facts=refactoring_image_keys,
    openstack_network_facts=refactoring_network_keys,
    openstack_port_facts=refactoring_port_keys,
    openstack_server_facts=refactoring_server_keys,
    openstack_subnet_facts=refactoring_subnet_keys

)
