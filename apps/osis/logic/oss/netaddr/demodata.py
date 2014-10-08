
def populate():
    import random, time
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.netaddr
    
    for i in range(10):
        obj = client.new()
        obj.ipaddr = "127.0.0.%s"%i
        obj.ipaddr6 = "N/A"
        obj.description = 'some description'
        obj.supportremarks = 'Remarks'

        for x in range(0, random.randint(1, 4)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the netaddr comment'
            comment.time = int(time.time())

        client.set(obj)