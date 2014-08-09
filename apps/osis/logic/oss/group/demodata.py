
def populate():
    import random
    import time
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.group

    for i in range(10):
        obj = client.new()
        obj.name = "kristof %s " % i
        obj.members = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
        obj.acl = {'admin': 'R/W/E'}

        for x in range(0, random.randint(1, 3)):
            cont = obj.new_contact()
            cont.type = "email"
            cont.value = "email%s.com" % i

        for x in range(0, random.randint(1, 4)):
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the group comment'
            comment.time = int(time.time())

        for x in range(0, random.randint(1, 4)):
            datasource = obj.new_datasource()
            datasource.name = 'datasource %s' % x


        client.set(obj)
