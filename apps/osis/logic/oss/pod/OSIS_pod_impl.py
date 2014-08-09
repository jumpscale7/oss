from JumpScale import j
from pymongo import MongoClient

parentclass=j.core.osis.getOsisImplementationParentClass("oss")  #is the name of the namespace


class mainclass(parentclass):
    """
    """
    def setPreSave(self, value):
        osscl = MongoClient()
        db = osscl['oss']
        orgcl = db['organization']
        organizationid = value.get('organization')
        if organizationid:
            org = orgcl.find_one({'id': organizationid})
            value['organization_name'] = org.get('name', organizationid) if org else organizationid

        datacentercl = db['datacenter']
        datacenterid = value.get('datacenter')
        if datacenterid:
            datacenter = datacentercl.find_one({'id': datacenterid})
            value['datacenter_name'] = datacenter.get('name', datacenterid) if datacenter else datacenterid

        commentors = [comment['author'] for comment in value['comments']]
        if commentors:
            usercl = db['user']
            value['comments'] = list()
            for commentor in commentors:
                user = usercl.find_one({'id': commentor})
                value['comments'].append(user.get('name', commentor) if user else commentor)

        return value
