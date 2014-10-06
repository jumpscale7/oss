from JumpScale import j
import JumpScale.lib.txtrobot
import JumpScale.grid.osis
import ujson as json


initcmds="""

ticket (issue,bug,feature,task,event,perfissue,check)
- create (c,n,new,update,u)
-- id
-- name
-- description
-- project #as name
-- who #name of person who will do it (email or username)
-- prio #0-4,4 being highest, see below
-- descr (description,d)
-- parent #specify part of name or id of task which we are subtask for
-- depends #specify part of name or id of task which we depend on, do comma separated if more than 1
-- deadline
-- duplicate #comma separated list of id's 
-- source #id or name or email of person who created the ticket
-- sprint #id or (part of name) name of sprint
-- organization #id or (part of name) name of organization
-- nextstep #epoch or time from now notation (e.g. +4d, +1m)
-- jobs #list of ids to jobs
-- time_created         #epoch
-- time_lastmessage     #epoch
-- time_lastresponse    #epoch
-- time_closed          #epoch
-- datasources #comma separated list of datasources e.g. osticket, ...
-- acl                  #as tags 'admin:RW guest:R'
-- params               #json repr of dict with args or as tags (if possible)

- export #produce list of ticket.create statements defined above
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of org 
-- name #name or part of name of org (if id not used)
-- comment
-- created
-- author

- assign
-- id
-- who

- duplicate
-- id

- get #produces full ticket statement, see above)
-- id

- message
-- id
-- ticketid
-- subject
-- message
-- destination #as comma separated
-- time #epoch
-- type #email;sms;gtalk;tel

- depend
-- id
-- name (n) #speciy name or part of name
-- on #depend on (speciy name or part of name or id)

- subtask
-- id
-- name (n) #speciy name or part of name (if id not used)
-- parent #parent of this task (speciy name or part of name or id)

- duplicate
-- id
-- name (n) #speciy name or part of name (if id not used) of ticket
-- duplicate #duplicate (speciy name or part of name or id)

##############################################################################
organization
- create (c,n,new,update,u)
-- name
-- id
-- description
-- companyname
-- parent #specify part of name or id of organization
-- vatnr
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- address
-- id #id of org 
-- name #name or part of name of org (if id not used)
-- country
-- city
-- citycode
-- street
-- nr

- contact
-- id #id of org
-- name #name or part of name of org (if id not used)
-- type #phone;mobile;email;skype
-- value

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of org 
-- name #name or part of name of org (if id not used)
-- comment
-- created
-- author

##############################################################################
user
- create (c,n,new,update,u)
-- name
-- id
-- organization
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- address
-- id #id of user 
-- name #name or part of name of user (if id not used)
-- country
-- city
-- citycode
-- street
-- nr

- contact
-- id #id of user
-- name #name or part of name of user (if id not used)
-- type #phone;mobile;email;skype
-- value

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of user 
-- name #name or part of name of user (if id not used)
-- comment
-- created
-- author


##############################################################################
group
- create (c,n,new,update,u)
-- name
-- id
-- members #comma separated list of members, member is group defined as id, or name or part of name or even email
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- contact
-- id #id of group
-- name #name or part of name of group (if id not used)
-- type #phone;mobile;email;skype
-- value

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
project
- create (c,n,new,update,u)
-- name
-- description
-- organizations #comma separated list of orgs (as id, name part of name)
-- deadline #as epoch or as future notation  e.g. +4d
-- id
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author


##############################################################################
sprint
- create (c,n,new,update,u)
-- name
-- description
-- organizations #comma separated list of orgs (as id, name part of name)
-- start #as epoch or as future notation  e.g. +4d
-- stop #as epoch or as future notation  e.g. +4d
-- id
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
datacenter
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization #id of org which owns the dc
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- address
-- id #id of datacenter 
-- name #name or part of name of datacenter (if id not used)
-- country
-- city
-- citycode
-- street
-- nr

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
pod
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organizations #comma separated list of orgs (as id, name part of name)
-- datacenters #comma separated list of datacenters (as id, name part of name)
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
rack
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization #comma separated list of orgs (as id, name part of name)
-- datacenter #comma separated list of datacenters (as id, name part of name, part of label)
-- pod #comma separated list of pods (as id, name part of name, part of label)
-- datasources #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
asset
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- organization
-- rack #as id name or part of name or part of label
-- U    #height in U
-- pos (position,rackpos)  #position in rack in U from bottomn
-- brand
-- model
-- type
-- parent       #id,name or label (or part of) of parent asset
-- depends      #comma separated list of id's or names/labels of assets depend on 
-- datasources  #comma separated list of datasources
-- acl                  #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##############################################################################
machine
- create (c,n,new,update,u)
-- id
-- name
-- label
-- description
-- memory
-- ssdcapacity
-- hdcapacity
-- cpumhz
-- nrcores
-- nrcpu
-- organization    #comma separated list of orgs (as id, name part of name)
-- interfaces       #comma separated list of interfaceids
-- assethost        #name, part of name, id, label, part of label of asset
-- parent           #name, part of name, id, label, part of label of machine
-- type
-- depends          #comma separed list of machines we depend on (name, part of name, id, label, part of label of machine)
-- acl              #as tags 'admin:RW guest:R'

- export 
-- filter (f) #is filter which is query str for osis

- list (l)
-- max #max amount of items
-- start #startpoint e.g. 10 is id
-- filter (f) #is filter which is query str for osis
-- verbose (v) #1-3 3 being most verbose

- delete (d,del)
-- id

- comment
-- id #id of group 
-- name #name or part of name of group (if id not used)
-- comment
-- created
-- author

##################################################################################
priorities:
  Show-stopper:4
  Critical:3
  Major:2
  Normal:1
  Minor:0

"""

class OSSFactory(object):

    def get(self):
        robot=j.tools.txtrobot.get(initcmds)
        cmds=OSSRobotCmds()
        robot.addCmdClassObj(cmds)
        return robot

class OSSRobotCmds():
    def __init__(self):
        self.osscl = j.core.osis.getClientForNamespace('oss')

    def organization__create(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        else:
            organization = self.osscl.organization.new()
        organization.name = args.get('name')
        organization.description = args.get('description')
        organization.companyname = args.get('companyname')
        organization.parent = args.get('parent')
        organization.vatnr = args.get('vatnr')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            organization.acl = tags.getDict()
        self.osscl.organization.set(organization)
        return 'Organization was created/updated successfully'

    def organization__address(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        elif args.get('name'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('name')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        address = organization.new_address()
        address.country = args.get('country')
        address.city = args.get('city')
        address.citycode = args.get('citycode')
        address.street = args.get('street')
        address.nr = args.get('nr')
        self.osscl.organization.set(organization)
        return 'Organization address was added successfully'

    def organization__contact(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        elif args.get('name'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('name')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        contact = organization.new_contact()
        contact.type = args.get('type')
        contact.value = args.get('value')
        self.osscl.organization.set(organization)
        return 'Organization contact was added successfully'

    def organization__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.organization.simpleSearch(q, start, size)

    def organization__delete(self, **args):
        self.osscl.organization.delete(int(args.get('id')))
        return 'Organization was deleted successfully'

    def organization__comment(self, **args):
        if args.get('id'):
            if not self.osscl.organization.exists(int(args.get('id'))):
                return 'Organization with ID %s was not found.' % args.get('id')
            organization = self.osscl.organization.get(int(args.get('id')))
        elif args.get('name'):
            organization = self.osscl.organization.simpleSearch({'name': args.get('name')})
            if organization:
                organization = self.osscl.organization.get(organization[0]['id'])
            else:
                return 'Organization with name %s can not be found' % args.get('name')
        else:
            return 'Organization ID or name must be passed'
        comment = organization.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.organization.set(organization)
        return 'Organization comment was added successfully'

    def group__create(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        else:
            group = self.osscl.group.new()
        group.name = args.get('name')
        group.members = args.get('members')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            group.acl = tags.getDict()
        self.osscl.group.set(group)
        return 'Group was created/updated successfully'

    def group__contact(self, **args):
        if args.get('id'):
            if not self.osscl.group.exists(int(args.get('id'))):
                return 'Group with ID %s was not found.' % args.get('id')
            group = self.osscl.group.get(int(args.get('id')))
        elif args.get('name'):
            group = self.osscl.group.simpleSearch({'name': args.get('name')})
            if group:
                group = self.osscl.group.get(group[0]['id'])
            else:
                return 'Group with name %s can not be found' % args.get('name')
        else:
            return 'Group ID or name must be passed'
        contact = group.new_contact()
        contact.type = args.get('type')
        contact.value = args.get('value')
        self.osscl.group.set(group)
        return 'Group contact was added successfully'

    def group__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.group.simpleSearch(q, start, size)

    def group__delete(self, **args):
        self.osscl.group.delete(int(args.get('id')))
        return 'Group was deleted successfully'

    def project__create(self, **args):
        if args.get('id'):
            if not self.osscl.project.exists(int(args.get('id'))):
                return 'Project with ID %s was not found.' % args.get('id')
            project = self.osscl.project.get(int(args.get('id')))
        else:
            project = self.osscl.project.new()
        project.name = args.get('name')
        project.descr = args.get('description')
        project.organizations = args.get('organizations')
        project.deadline = args.get('deadline')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            project.acl = tags.getDict()
        self.osscl.project.set(project)
        return 'Project was created/updated successfully'

    def project__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.project.simpleSearch(q, start, size)

    def project__delete(self, **args):
        self.osscl.project.delete(int(args.get('id')))
        return 'Project was deleted successfully'

    def project__comment(self, **args):
        if args.get('id'):
            if not self.osscl.project.exists(int(args.get('id'))):
                return 'Project with ID %s was not found.' % args.get('id')
            project = self.osscl.project.get(int(args.get('id')))
        elif args.get('name'):
            project = self.osscl.project.simpleSearch({'name': args.get('name')})
            if project:
                project = self.osscl.project.get(project[0]['id'])
            else:
                return 'Project with name %s can not be found' % args.get('name')
        else:
            return 'Project ID or name must be passed'
        comment = project.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.project.set(project)
        return 'Project comment was added successfully'

    def user__create(self, **args):
        user = self.osscl.user.new()
        userdata = user.dump()
        for arg in args:
            if arg in userdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    userdata['acl'] = tags.getDict()
                else:
                    userdata[arg] = args.get(arg)
        user.dict2obj(userdata)
        self.osscl.user.set(user)
        return 'User was added successfully'

    def ticket__create(self, **args):
        ticket = self.osscl.ticket.new()
        ticketdata = ticket.dump()
        for arg in args:
            if arg in ticketdata:
                if arg == 'acl':
                    tags = j.core.tags.getObject(args.get('acl'))
                    ticketdata['acl'] = tags.getDict()
                else:
                    ticketdata[arg] = args.get(arg)
        ticket.dict2obj(ticketdata)
        self.osscl.ticket.set(ticket)
        return 'Ticket was added successfully'

    def ticket__list(self, **args):
        maximum = args.get('max')
        start = args.get('start', 0)
        query = json.loads(args.get('filter', "{}"))
        tickets = self.osscl.ticket.simpleSearch(query, size=maximum, start=start)
        result = list()
        verbose = int(args.get('verbose'), 3)
        if verbose>3:
            verbose=3
        else:
            verbose=1
        if verbose>1:
            for ticket in tickets:
                result.append(ticket.dump()) 
        else:
            out=""
            for ticket in tickets:
                out+="%-7s %-15s %-10s %s\n"%(ticket.id,ticket.name,ticket.description,ticket.type)
            result=out
        return result

    def ticket__delete(self, **args):
        self.osscl.ticketid.delete(int(args.get('id')))
        return 'Ticket was deleted successfully'

    def ticket__assign(self, **args):
        assignee = args.get('who')
        ticket = self.osscl.ticket.get(int(args.get('id')))
        ticket.taskowner = assignee
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__duplicate(self, **args):
        tkt = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        duplicate = args.get('duplicate')
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        ticket['duplicate'].append(int(duplicate))
        tkt.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__depend(self, **args):
        tkt = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        depend = args.get('on')
        ticket['depends'].append(int(depend))
        tkt.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__subtask(self,**args):
        tkt = self.osscl.ticket.new()
        id = args.get('id')
        query = {'id':id}
        if not id:
            name = args.get('name')
            query = {'name': '*%s*' % name}
        ticket = self.osscl.ticket.simpleSearch({}, partials=query)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket[0]
        parent = args.get('parent')
        ticket['parent'] = int(parent)
        tkt.dict2obj(ticket)
        self.osscl.ticket.set(ticket)
        return 'Ticket was updated successfully'

    def ticket__get(self,**args):
        id = args.get('id')
        ticket = self.osscl.ticket.get(id)
        if not ticket:
            return 'Ticket not found'
        ticket = ticket.dump()
        out = 'Ticket:\n'
        for k, v in ticket.iteritems():
            out += '%s: %s\n' % (k, v)
        return out

    def sprint__create(self, **args):
        if args.get('id'):
            if not self.osscl.sprint.exists(int(args.get('id'))):
                return 'Sprint with ID %s was not found.' % args.get('id')
            sprint = self.osscl.sprint.get(int(args.get('id')))
        else:
            sprint = self.osscl.sprint.new()
        sprint.name = args.get('name')
        sprint.description = args.get('description')
        sprint.organizations = args.get('organizations')
        sprint.start = args.get('start')
        sprint.stop = args.get('stop')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            sprint.acl = tags.getDict()
        self.osscl.sprint.set(sprint)
        return 'Sprint was created/updated successfully'

    def sprint__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.sprint.simpleSearch(q, start, size)

    def sprint__delete(self, **args):
        self.osscl.sprint.delete(int(args.get('id')))
        return 'Sprint was deleted successfully'

    def sprint__comment(self, **args):
        if args.get('id'):
            if not self.osscl.sprint.exists(int(args.get('id'))):
                return 'Sprint with ID %s was not found.' % args.get('id')
            sprint = self.osscl.sprint.get(int(args.get('id')))
        elif args.get('name'):
            sprint = self.osscl.sprint.simpleSearch({'name': args.get('name')})
            if sprint:
                sprint = self.osscl.sprint.get(sprint[0]['id'])
            else:
                return 'Sprint with name %s can not be found' % args.get('name')
        else:
            return 'Sprint ID or name must be passed'
        comment = sprint.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.sprint.set(sprint)
        return 'Sprint comment was added successfully'

    def datacenter__create(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        else:
            datacenter = self.osscl.datacenter.new()
        datacenter.name = args.get('name')
        datacenter.description = args.get('description')
        datacenter.label = args.get('label')
        datacenter.organization = args.get('organization')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            datacenter.acl = tags.getDict()
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter was created/updated successfully'

    def datacenter__address(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        address = datacenter.new_address()
        address.country = args.get('country')
        address.city = args.get('city')
        address.citycode = args.get('citycode')
        address.street = args.get('street')
        address.nr = args.get('nr')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter address was added successfully'

    def datacenter__contact(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        contact = datacenter.new_contact()
        contact.type = args.get('type')
        contact.value = args.get('value')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter contact was added successfully'

    def datacenter__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.datacenter.simpleSearch(q, start, size)

    def datacenter__delete(self, **args):
        self.osscl.datacenter.delete(int(args.get('id')))
        return 'Datacenter was deleted successfully'

    def datacenter__comment(self, **args):
        if args.get('id'):
            if not self.osscl.datacenter.exists(int(args.get('id'))):
                return 'Datacenter with ID %s was not found.' % args.get('id')
            datacenter = self.osscl.datacenter.get(int(args.get('id')))
        elif args.get('name'):
            datacenter = self.osscl.datacenter.simpleSearch({'name': args.get('name')})
            if datacenter:
                datacenter = self.osscl.datacenter.get(datacenter[0]['id'])
            else:
                return 'Datacenter with name %s can not be found' % args.get('name')
        else:
            return 'Datacenter ID or name must be passed'
        comment = datacenter.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.datacenter.set(datacenter)
        return 'Datacenter comment was added successfully'

    def pod__create(self, **args):
        if args.get('id'):
            if not self.osscl.pod.exists(int(args.get('id'))):
                return 'Pod with ID %s was not found.' % args.get('id')
            pod = self.osscl.pod.get(int(args.get('id')))
        else:
            pod = self.osscl.pod.new()
        pod.name = args.get('name')
        pod.description = args.get('description')
        pod.label = args.get('label')
        pod.organizations = args.get('organizations')
        pod.datacenters = args.get('datacenters')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            pod.acl = tags.getDict()
        self.osscl.pod.set(pod)
        return 'Pod was created/updated successfully'

    def pod__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.pod.simpleSearch(q, start, size)

    def pod__delete(self, **args):
        self.osscl.pod.delete(int(args.get('id')))
        return 'Pod was deleted successfully'

    def pod__comment(self, **args):
        if args.get('id'):
            if not self.osscl.pod.exists(int(args.get('id'))):
                return 'Pod with ID %s was not found.' % args.get('id')
            pod = self.osscl.pod.get(int(args.get('id')))
        elif args.get('name'):
            pod = self.osscl.pod.simpleSearch({'name': args.get('name')})
            if pod:
                pod = self.osscl.pod.get(pod[0]['id'])
            else:
                return 'Pod with name %s can not be found' % args.get('name')
        else:
            return 'Pod ID or name must be passed'
        comment = pod.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.pod.set(pod)
        return 'Pod comment was added successfully'

    def rack__create(self, **args):
        if args.get('id'):
            if not self.osscl.rack.exists(int(args.get('id'))):
                return 'Rack with ID %s was not found.' % args.get('id')
            rack = self.osscl.rack.get(int(args.get('id')))
        else:
            rack = self.osscl.rack.new()
        rack.name = args.get('name')
        rack.description = args.get('description')
        rack.label = args.get('label')
        rack.organization = args.get('organizations')
        rack.datacenter = args.get('datacenters')
        rack.pod = args.get('pods')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            rack.acl = tags.getDict()
        self.osscl.rack.set(rack)
        return 'Rack was created/updated successfully'

    def rack__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.rack.simpleSearch(q, start, size)

    def rack__delete(self, **args):
        self.osscl.rack.delete(int(args.get('id')))
        return 'Rack was deleted successfully'

    def rack__comment(self, **args):
        if args.get('id'):
            if not self.osscl.rack.exists(int(args.get('id'))):
                return 'Rack with ID %s was not found.' % args.get('id')
            rack = self.osscl.rack.get(int(args.get('id')))
        elif args.get('name'):
            rack = self.osscl.rack.simpleSearch({'name': args.get('name')})
            if rack:
                rack = self.osscl.rack.get(rack[0]['id'])
            else:
                return 'Rack with name %s can not be found' % args.get('name')
        else:
            return 'Rack ID or name must be passed'
        comment = rack.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.rack.set(rack)
        return 'Rack comment was added successfully'

    def asset__create(self, **args):
        if args.get('id'):
            if not self.osscl.asset.exists(int(args.get('id'))):
                return 'Asset with ID %s was not found.' % args.get('id')
            asset = self.osscl.asset.get(int(args.get('id')))
        else:
            asset = self.osscl.asset.new()
        asset.name = args.get('name')
        asset.description = args.get('description')
        asset.label = args.get('label')
        asset.rack = args.get('rack')
        asset.U = args.get('U')
        asset.rackpos = args.get('pos')
        asset.brand = args.get('brand')
        asset.model = args.get('model')
        asset.type = args.get('type')
        asset.parent = args.get('parent')
        asset.depends = args.get('depends')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            asset.acl = tags.getDict()
        self.osscl.asset.set(asset)
        return 'Asset was created/updated successfully'

    def asset__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.asset.simpleSearch(q, start, size)

    def asset__delete(self, **args):
        self.osscl.asset.delete(int(args.get('id')))
        return 'Asset was deleted successfully'

    def asset__comment(self, **args):
        if args.get('id'):
            if not self.osscl.asset.exists(int(args.get('id'))):
                return 'Asset with ID %s was not found.' % args.get('id')
            asset = self.osscl.asset.get(int(args.get('id')))
        elif args.get('name'):
            asset = self.osscl.asset.simpleSearch({'name': args.get('name')})
            if asset:
                asset = self.osscl.asset.get(asset[0]['id'])
            else:
                return 'Asset with name %s can not be found' % args.get('name')
        else:
            return 'Asset ID or name must be passed'
        comment = asset.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.asset.set(asset)
        return 'Asset comment was added successfully'

    def machine__create(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        else:
            machine = self.osscl.machine.new()
        machine.name = args.get('name')
        machine.description = args.get('description')
        machine.label = args.get('label')
        machine.memory = int(args.get('memory')) if args.get('memory') else 0
        machine.ssdcapacity = int(args.get('ssdcapacity')) if args.get('ssdcapacity') else 0
        machine.hdcapacity = int(args.get('hdcapacity')) if args.get('hdcapacity') else 0
        machine.cpumhz = int(args.get('cpumhz')) if args.get('cpumhz') else 0
        machine.nrcores = int(args.get('nrcores')) if args.get('nrcores') else 0
        machine.nrcpu = int(args.get('nrcpu')) if args.get('nrcpu') else 0
        machine.organization = args.get('organization')
        machine.interfaces = args.get('interfaces')
        machine.assethost = int(args.get('assethost')) if args.get('assethost') else 0
        machine.parent = int(args.get('parent')) if args.get('parent') else 0
        machine.type = args.get('type')
        machine.depends = args.get('depends')
        # TODO set data sources
        if args.get('acl'):
            tags = j.core.tags.getObject(args.get('acl'))
            machine.acl = tags.getDict()
        self.osscl.machine.set(machine)
        return 'Machine was created/updated successfully'

    def machine__list(self, **args):
        q = dict()
        if args.get('filter'):
            q = json.loads(args.get('filter'))
        start = int(args.get('start')) if args.get('start') else 0
        size = int(args.get('max')) if args.get('max') else None
        return self.osscl.machine.simpleSearch(q, start, size)

    def machine__delete(self, **args):
        self.osscl.machine.delete(int(args.get('id')))
        return 'Machine was deleted successfully'

    def machine__comment(self, **args):
        if args.get('id'):
            if not self.osscl.machine.exists(int(args.get('id'))):
                return 'Machine with ID %s was not found.' % args.get('id')
            machine = self.osscl.machine.get(int(args.get('id')))
        elif args.get('name'):
            machine = self.osscl.machine.simpleSearch({'name': args.get('name')})
            if machine:
                machine = self.osscl.machine.get(machine[0]['id'])
            else:
                return 'Machine with name %s can not be found' % args.get('name')
        else:
            return 'Machine ID or name must be passed'
        comment = machine.new_comment()
        comment.comment = args.get('comment')
        comment.time = args.get('created')
        comment.author = args.get('author')
        self.osscl.machine.set(machine)
        return 'Machine comment was added successfully'