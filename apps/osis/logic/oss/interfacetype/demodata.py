
def populate():
    import JumpScale.grid.osis
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.interfacetype
    
    for i in range(10):
        obj=client.new()
        obj.type="type%s"%i
        obj.description="this is a random description"
        client.set(obj)