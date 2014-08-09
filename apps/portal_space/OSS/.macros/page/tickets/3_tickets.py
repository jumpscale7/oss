
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Project', 'Task Owner', 'Deadline']
    fieldvalues = ['[%(id)s|/oss/ticket?id=%(id)s]', "name", '[%(project_name)s|/oss/project?id=%(project)s]', '[%(taskowner_name)s|/oss/user?id=%(taskowner)s]', modifier.makeTime]
    fieldids = ['id', "name", 'project', 'taskowner', 'deadline']
    tableid = modifier.addTableForModel('oss', 'ticket', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
