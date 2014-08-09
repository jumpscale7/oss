
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Name', 'Description']
    fieldvalues = ['[%(id)s|/oss/sprint?id=%(id)s]', "name", 'description']
    fieldids = ['id', "name", 'description']
    tableid = modifier.addTableForModel('oss', 'sprint', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
