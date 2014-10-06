import JumpScale.grid.osis

def populate():
    import random
    import time
    client = j.core.osis.getClientForNamespace('oss')
    client = client.pod

    for i in range(10):
        obj = client.new()
        obj.name = "pod%s" % i
        obj.label = 'label %s' % i
        obj.organization = random.randint(1,5)
        obj.datacenter = random.randint(1,5)
        obj.description = 'This is a description'
        obj.acl = {'admin': 'R/W/E'}
        for x in range(0, random.randint(1,3)):
            comment = obj.new_comment()
            comment.comment = 'this is the comment'
            comment.time = int(time.time())
            comment.author = random.randint(1,9)
        client.set(obj)
