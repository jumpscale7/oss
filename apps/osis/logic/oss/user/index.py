
def index(client):
    client.ensure_index("guid")
    client.ensure_index("name")
    client.ensure_index("organization")
    print "index done"
    
