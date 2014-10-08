
def populate():
    import random
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.rack

    for i in range(10):
        obj = client.new()
        obj.organization = random.randint(1,20)
        obj.description = 'some machine description'
        obj.location = "location abcd%s" % i
        client.set(obj)