
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    def makelist(row, field):
        return ' ,'.join(row[field])

    fieldnames = ['ID', 'Name', 'Description', 'Organizations']
    fieldvalues = ['[%(id)s|/oss/project?id=%(id)s]', "name", 'descr', makelist]
    fieldids = ['id', "name", 'descr', 'organizations_names']
    tableid = modifier.addTableForModel('oss', 'project', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
