
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)


    fieldnames = ['ID', 'Name', 'Company Name', 'Description']
    fieldvalues = ['[%(id)s|/oss/organization?id=%(id)s]', "name", 'companyname', 'description']
    fieldids = ['id', "name", 'companyname', 'description']
    tableid = modifier.addTableForModel('oss', 'organization', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
