from JumpScale import j
from pymongo import MongoClient

parentclass=j.core.osis.getOsisImplementationParentClass("oss")  #is the name of the namespace


class mainclass(parentclass):
    """
    """
    def setPreSave(self, value):
        osscl = MongoClient()
        db = osscl['oss']
        usercl = db['user']
        members = value.get('members')
        value['members_name'] = list()
        if members:
            for member in members:
                user = usercl.find_one({'id': member})
                value['members_name'].append(user.get('name', member) if user else member)

        return value

