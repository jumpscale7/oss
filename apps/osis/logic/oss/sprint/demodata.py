
def populate():
    import JumpScale.grid.osis
    import time, random
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.sprint
    
    for i in range(20):
        obj=client.new()
        obj.name="test sprint %s" % i
        obj.description="test sprint %s" % i
        obj.organizations=[random.randint(1,20), random.randint(1,20), random.randint(1,20)]
        obj.start=int(time.time())
        obj.stop=int(time.time())
        obj.acl = {'admin': 'R/W/E'}
        for x in range(0, random.randint(1, 4)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the sprint comment'
            comment.time = int(time.time())
        client.set(obj)