
def populate():
    import random, time
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.machine

    for i in range(10):
        obj = client.new()
        obj.name = 'Machine name %s' % i
        obj.organization = random.randint(1,20)
        obj.description = 'some machine description'
        obj.label = "label%s" % i
        obj.parent = random.randint(1,20)
        obj.type = "type%s" % i

        for k in range(random.randint(1,3)):
            interface = obj.new_interface()
            interface.type = 'interfacetype%s' % random.randint(1,20)
            interface.macaddr = "02:00:00:00:01:%s" % k
            interface.vlanid = "vlan%s" % random.randint(1,20)
            interface.vxlanid = "vxlan%s" % random.randint(1,20)
            interface.description = 'some description'
            interface.organization = random.randint(1,20)
            netaddr = interface.new_netaddr()
            netaddr.ipaddr = "127.0.0.%s"%i
            netaddr.ipaddr6 = "N/A"
            netaddr.description = 'some description'
            interface.connects = [random.randint(1,20), random.randint(1,20)]

        obj.depends = [random.randint(1,20), random.randint(1,20)]
        obj.assethost = random.randint(1,20)
        obj.memory = 10000
        obj.ssdcapacity = 16
        obj.hdcapacity = 20
        obj.cpumhz = 380
        obj.nrcores = 4
        obj.nrcpu = 2
        obj.acl = {'admin':'R/W/E'}

        for x in range(0, random.randint(1, 4)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the machine comment'
            comment.time = int(time.time())

        client.set(obj)