
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Ticket Type', 'Description']
    fieldvalues = ['[%(id)s|/oss/workflow?id=%(id)s]', "name", "tickettype", "description"]
    fieldids = ['id', "name", "tickettype", "description"'deadline']
    tableid = modifier.addTableForModel('oss', 'workflow', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
