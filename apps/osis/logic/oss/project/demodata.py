
def populate():
    import JumpScale.grid.osis
    import time
    import random
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.project

    for i in range(20):
        obj=client.new()
        obj.name="test proj %s" % i
        obj.descr="test proj %s" % i
        obj.organizations=['test org %s' % random.randint(1, 20)]
        obj.deadline=int(time.time())
        obj.acl = {'admin':'R/W/E'}

        for x in range(0, random.randint(0,3)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the project comment'
            comment.time = int(time.time())

        client.set(obj)