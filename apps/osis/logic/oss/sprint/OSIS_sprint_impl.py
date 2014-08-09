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
        organizationids = value.get('organizations')
        value['organization_names'] = list()
        if organizationids:
            for org in organizationids:
                organization = orgcl.find_one({'id': org})
                value['organization_names'].append(organization.get('name', org) if organization else org)

        return value

