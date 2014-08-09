
def populate():
    import JumpScale.grid.osis
    import time
    import random
    osscl = j.core.osis.getClientForNamespace('oss')
    client = osscl.organization
    
    for i in range(20):
        obj=client.new()
        obj.name="test org %s" % i
        obj.description="test org %s" % i
        obj.companyname='test company'
        obj.parent=random.randint(1,20)
        obj.vatnr = 'VAT NUMBER'
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