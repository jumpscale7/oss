
def populate():
    import random, time
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.asset

    for i in range(10):
        obj = client.new()
        obj.organization = random.randint(1,20)
        obj.description = 'some description'
        obj.label = "label%s" % i
        obj.parent = random.randint(1,20)
        obj.type = "type%s" % i
        obj.brand = 'Brand x'
        obj.model = 'X500'

        for x in range(0, random.randint(1,4)):
            component = obj.new_component()
            component.brand = 'Brand Y'
            component.model = 'X50%s' % x
            component.nr = 5+x
            component.description = 'component description'
            component.supportremarks = 'some remarks'
            compcomment = component.new_comment()
            compcomment.author = random.randint(1,5)
            compcomment.comment = 'this is the component comment'
            compcomment.time = int(time.time())

        for x in range(0, random.randint(1,4)):
            interface = obj.new_interface()
            interface.type = 'interfacetype %s' % x
            interface.macaddr = "02:00:00:00:01:23"
            interface.vlanid = "vlan%s" % random.randint(1,20)
            interface.vxlanid = "vxlan%s" % random.randint(1,20)
            interface.description = 'some description'
            interface.organization = random.randint(1,20)
            netaddr = interface.new_netaddr()
            netaddr.ipaddr = "127.0.0.%s"%i
            netaddr.ipaddr6 = "N/A"
            netaddr.description = 'some description'
            interface.connects = [random.randint(1,20), random.randint(1,20)]

        for x in range(0, random.randint(1,4)):
            comment = obj.new_comment()
            comment.author = random.randint(1,5)
            comment.comment = 'this is the asset comment'
            comment.time = int(time.time())

        obj.depends = [random.randint(1,20), random.randint(1,20)]
        obj.rackid = random.randint(1,9)
        obj.U = random.randint(5,10)
        obj.rackpos = random.randint(1,10)
        client.set(obj)