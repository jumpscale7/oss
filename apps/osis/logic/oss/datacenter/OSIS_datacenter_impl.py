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
            value['organization_names'] = org.get('name', organizationid) if org else organizationid

        return value



