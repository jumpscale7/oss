
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Type', 'Description']
    fieldvalues = ['id', 'type', 'description']
    fieldids = ['id', 'type', 'description']
    tableid = modifier.addTableForModel('oss', 'assettype', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
