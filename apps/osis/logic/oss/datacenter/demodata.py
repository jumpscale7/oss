import JumpScale.grid.osis

def populate():
    client = j.core.osis.getClientForNamespace('oss')
    client = client.datacenter
    import random

    for i in range(20):
        obj = client.new()
        obj.name = 'data center %s' % i
        obj.organization = random.randint(0,19)
        obj.description = "test description %s" % i

        for x in range(0, i):
            address = obj.new_addresse()
            address.country='Egypt'
            address.city='Cairo'
            address.citycode='CA'
            address.street='demo street'
            address.nr=15
        client.set(obj)
