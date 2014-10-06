
def populate():
    import JumpScale.grid.osis
    import time
    import random
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.message
    
    for i in range(20):
        obj=client.new()
        obj.id=i
        obj.subject="test subject %s" % i
        obj.message="test message %s" % i
        obj.time=int(time.time())
        obj.type="email"
        obj.ticket=random.randint(1, 20)
        client.set(obj)