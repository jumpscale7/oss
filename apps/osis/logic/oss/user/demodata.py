import JumpScale.grid.osis

def populate():
    import random, time
    client = j.core.osis.getClientForNamespace('oss')
    client = client.user

    for i in range(10):
        obj = client.new()
        obj.name = "kristof%s" % i
        obj.organization = "org1"
        obj.acl = {'admin': 'R/W/E'}

        for x in range(0, random.randint(0,3)):
            address = obj.new_addresse()
            address.country='Egypt'
            address.city='Cairo'
            address.citycode='CA'
            address.street='demo street'
            address.nr=15
            contact=obj.new_contact()
            contact.type='email'
            contact.value='test@test.com'
            contact=obj.new_contact()
            contact.type='skype'
            contact.value='test_skype'
            datasource = obj.new_datasource()
            datasource.name = 'datasource %s' % x
            comment = obj.new_comment()
            comment.author = random.randint(1, 5)
            comment.comment = 'this is the organization comment'
            comment.time = int(time.time())
        client.set(obj)