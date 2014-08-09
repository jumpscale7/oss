from JumpScale import j
from pymongo import MongoClient

parentclass=j.core.osis.getOsisImplementationParentClass("oss")  #is the name of the namespace


class mainclass(parentclass):
    """
    """

    def setPreSave(self, value):
        osscl = MongoClient()
        db = osscl['oss']
        podcl = db['pod']
        podid = value.get('pod')
        if podid:
            value['project_name'] = podcl.find_one({'id': podid}).get('name')

        datacentercl = osscl['datacenter']
        datacenterid = value.get('datacenter')
        if datacenterid:
            datacenter = datacentercl.find_one({'id': datacenterid})
            value['datacenter_name'] = datacenter.get('name') if datacenter else datacenterid

        db = osscl['oss']
        orgcl = db['organization']
        organizationid = value.get('organization')
        if organizationid:
            org = orgcl.find_one({'id': organizationid})
            value['organization_name'] = org.get('name') if org else organizationid

        return value

