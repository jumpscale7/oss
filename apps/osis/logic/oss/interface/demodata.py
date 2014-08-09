
def populate():
    import random, time
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.interface

    for i in range(10):
        obj = client.new()
        obj.type = "type %s" % i
        obj.macaddr = "02:00:00:00:01:23"
        obj.vlanid = "vlan%s" % random.randint(1,20)
        obj.vxlanid = "vxlan%s" % random.randint(1,20)
        obj.organization = random.randint(1,20)
        obj.description = 'some description'
        netaddr = obj.new_netaddr()
        netaddr.ipaddr = "127.0.0.%s"%i
        netaddr.ipaddr6 = "N/A"
        netaddr.description = 'some description'
        obj.connects = [random.randint(1,20), random.randint(1,20)]
        obj.brand = 'Brand X'
        obj.model = 'X500'
        obj.supportremarks = 'some remarks'

        for x in range(0, random.randint(1, 4)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the interface comment'
            comment.time = int(time.time())
        client.set(obj)