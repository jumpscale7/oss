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

        datacentercl = db['datacenter']
        datacenterid = value.get('datacenter_label')
        if datacenterid:
            datacenter = datacentercl.find_one({'id': datacenterid})
            value['datacenter_name'] = datacenter.get('name', datacenterid) if datacenter else datacenterid

        podcl = db['pod']
        podid = value.get('pod_label')
        if podid:
            pod = podcl.find_one({'id': podid})
            value['pod_name'] = pod.get('name', podid) if pod else pod

        rackcl = db['rack']
        rackid = value.get('rackid')
        if rackid:
            rack = rackcl.find_one({'id': rackid})
            value['rack_name'] = rack.get('name', rackid) if rack else rackid

        assetcl = db['asset']
        assetid = value.get('parent')
        if assetid:
            asset = assetcl.find_one({'id': assetid})
            value['parent_name'] = asset.get('name', assetid) if asset else assetid

        depends = value.get('depends')
        value['depends_names'] = list()
        for dep in depends:
            asset = assetcl.find_one({'id': assetid})
            value['depends_names'].append(asset.get('name', assetid) if asset else assetid)

        return value

