
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Name']
    fieldvalues = ['[%(id)s|/oss/group?id=%(id)s]', "name"]
    fieldids = ['id', "name"]
    tableid = modifier.addTableForModel('oss', 'group', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
