
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Name', 'Organization']
    fieldvalues = ['[%(id)s|/oss/user?id=%(id)s]', "name", 'organization']
    fieldids = ['id', "name", 'organization']
    tableid = modifier.addTableForModel('oss', 'user', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
