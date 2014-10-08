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
            #@todo this is wrong 
            value['organization_name'] = org.get('name', organizationid) if org else organizationid

        machinecl = db['machine']
        machineid = value.get('parent')
        if machineid:
            machine = machinecl.find_one({'id': machineid})
            #@todo this is wrong 
            value['parent_name'] = machine.get('name', machineid) if machine else machineid

        depends = value.get('depends')
        value['depends_names'] = list()
        for dep in depends:
            machine = machinecl.find_one({'id': dep})
            #@todo this is wrong 
            value['depends_names'].append(machine.get('name', str(dep)) if machine else dep)

        return value


