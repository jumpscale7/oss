
def populate():
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.brandtype

    for i in range(10):
        obj = client.new()
        obj.type = "type%s" % i
        obj.description = "this is a random description"
        obj.supportremarks = 'some remarks that are remarkable'
        client.set(obj)
