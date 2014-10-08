
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)


    fieldnames = ['ID', 'Organization', 'Description']
    fieldvalues = ['[%(id)s|/oss/datacenter?id=%(id)s]', "organization", 'description']
    fieldids = ['id', "organization", 'description']
    tableid = modifier.addTableForModel('oss', 'datacenter', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
