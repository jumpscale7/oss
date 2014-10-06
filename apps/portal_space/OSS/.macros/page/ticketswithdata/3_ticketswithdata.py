def main(j, args, params, tags, tasklet):
    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    def _formatdata(tickets):
        aaData = list()
        for ticket in tickets:
            itemdata = ['<a href=ticket?id=%s>%s</a>' % (ticket['id'], ticket['id'])]
            for field in ["name", "description", "priority"]:
                itemdata.append(str(ticket[field]))

            project = ossclient.project.simpleSearch({'id':ticket['project']})
            if not project:
                project = [{'id':None, 'name':'N/A'}]
            project = project[0]
            itemdata.insert(2, str('<a href=project?id=%s>%s</a>' % (project['id'], project.get('name', 'N/A'))))

            taskowner = ossclient.user.simpleSearch({'id':ticket['taskowner']})
            if not taskowner:
                taskowner = [{'id':None, 'name':'N/A'}]
            taskowner = taskowner[0]
            itemdata.insert(4, str('<a href=user?id=%s>%s</a>' % (taskowner['id'], taskowner.get('name', 'N/A'))))

            itemdata.append(j.base.time.epoch2HRDateTime(ticket["deadline"]))
            aaData.append(itemdata)
        aaData = str(aaData)
        return aaData.replace('[[', '[ [').replace(']]', '] ]')


    ossclient = j.core.osis.getClientForNamespace('oss')
    tickets = ossclient.ticket.simpleSearch(filters)
    tickets = _formatdata(tickets)

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ('ID', 'Name', 'Project', 'Description', 'Task Owner', 'Priority', 'Deadline')
    tableid = modifier.addTableFromData(tickets, fieldnames)

    modifier.addSearchOptions('#%s' % tableid)
    modifier.addSorting('#%s' % tableid, 0, 'desc')

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
