
def populate():
    import JumpScale.grid.osis
    import time
    import random
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.ticket

    for ttype in ('story', 'task', 'issue', 'event', 'bug', 'feature'):
        for i in range(5):
            obj = client.new()
            obj.name = "test ticket %s" % i
            obj.description = "test ticket %s" % i
            obj.priority = random.randint(1, 4)
            obj.project = random.randint(1, 5)
            obj.type = ttype
            obj.parent = random.randint(1, 10)
            obj.depends = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
            obj.deadline = int(time.time())
            obj.duplicate = [random.randint(1, 20), random.randint(1, 20)]
            obj.taskowner = random.randint(1, 10)
            obj.source = random.randint(1,10)
            obj.sprint = random.randint(1, 20)
            obj.organization = random.randint(1, 20)
            obj.nextstep = int(time.time())
            obj.workflow_name = 'testing'
            obj.job_status = 'ACTIVE'
            obj.time_created = int(time.time())
            obj.time_lastmessage = int(time.time())
            obj.time_lastresponse = int(time.time())
            obj.acl = {'admin': 'R/W/E'}
            obj.params = '{"1": 2, "3": 4}'

            for x in range(0, random.randint(1, 4)):
                comment = obj.new_comment()
                comment.author = random.randint(1, 5)
                comment.comment = 'this is the ticket comment'
                comment.time = int(time.time())

                message = obj.new_message()
                message.subject = 'message subject'
                message.description = ['a@b.com', 'a@bc.com']
                message.time = int(time.time())
                message.type = 'gtalk'
                message.ticket = random.randint(1,10)

                datasource = obj.new_datasource()
                datasource.name = 'datasource name'

            client.set(obj)
