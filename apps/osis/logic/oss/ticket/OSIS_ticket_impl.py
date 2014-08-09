from JumpScale import j
from pymongo import MongoClient

parentclass=j.core.osis.getOsisImplementationParentClass("oss")  #is the name of the namespace


class mainclass(parentclass):
    """
    """

    def setPreSave(self, value):
        osscl = MongoClient()
        db = osscl['oss']
        projcl = db['project']
        projectid = value.get('project')
        if projectid:
            project = projcl.find_one({'id': projectid})
            value['project_name'] = project.get('name', projectid) if project else projectid

        ticketcl = db['ticket']
        parentid = value.get('parent')
        if parentid:
            ticket = ticketcl.find_one({'id': parentid})
            value['parent_name'] = ticket.get('name', parentid) if ticket else parentid

        depends = value.get('depends')
        value['depends_names'] = list()
        for dep in depends:
            ticket = ticketcl.find_one({'id': dep})
            value['depends_names'].append(ticket.get('name', dep) if ticket else dep)

        duplicate = value.get('duplicate')
        value['duplicate_names'] = list()
        for dup in duplicate:
            ticket = ticketcl.find_one({'id': dup})
            value['duplicate_names'].append(ticket.get('name', dup) if ticket else dup)

        usercl = db['user']
        taskowner = value.get('taskowner')
        if taskowner:
            user = usercl.find_one({'id': taskowner})
            value['taskowner_name'] = user.get('name', taskowner) if user else taskowner

        source = value.get('source')
        if source:
            user = usercl.find_one({'id': source})
            value['source_name'] = user.get('name', source) if user else source

        sprintcl = db['sprint']
        sprintid = value.get('sprint')
        if sprintid:
            sprint = sprintcl.find_one({'id': sprintid})
            value['sprint_name'] = sprint.get('name', sprintid) if sprint else sprintid

        orgcl = db['organization']
        organizationid = value.get('organization')
        if organizationid:
            org = orgcl.find_one({'id': organizationid})
            value['organization_name'] = org.get('name', organizationid) if org else organizationid

        return value

