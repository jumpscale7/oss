import JumpScale.grid.osis

def populate():
    import random
    import time
    client = j.core.osis.getClientForNamespace('oss')
    client = client.job

    status = ['PENDING', 'ACTIVE', 'ERROR', 'OK', 'WARNING', 'CRITICAL']

    for i in range(10):
        obj = client.new()
        obj.name = "job %s" % i
        obj.startdate = int(time.time())
        obj.enddate = int(time.time())
        obj.status = status[random.randint(0,5)]
        for x in range(0, random.randint(2,3)):
            step = obj.new_step()
            step.name = 'job_step %s' % x
            step.startdate = int(time.time())
            step.enddate = int(time.time())
            step.warningtime = 1000
            step.criticaltime = 10000
            step.logs = 'logs'
            step.nextstep = 'no idea'
            step.status = 'OK'
            step.params = '{"anotherparam": "something", "time": "test"}'
        client.set(obj)
