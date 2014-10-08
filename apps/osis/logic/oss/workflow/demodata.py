import JumpScale.grid.osis

def populate():
    import random
    client = j.core.osis.getClientForNamespace('oss')
    client = client.workflow

    tickettypes = ['story', 'task', 'issue', 'event', 'bug', 'feature', 'ticket', 'perfissue', 'check', '']

    for i in range(10):
        obj = client.new()
        obj.name = "workflow%s" % i
        obj.tickettype = tickettypes[random.randint(0,9)]
        obj.description = 'This is a description'
        obj.acl = {'admin': 'R/W/E'}
        for x in range(0, random.randint(2,3)):
            step = obj.new_step()
            step.name = 'workflow_step %s' % x
            step.description = 'some description'
            step.warningtime = 1000
            step.criticaltime = 10000
            step.nextsteps = ['kill process', 'panic']
            step.nextsteps_error = ['no idea']
            step.jscript = '#this is an example jscript'
        client.set(obj)
