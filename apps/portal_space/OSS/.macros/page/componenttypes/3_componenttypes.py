

def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Type', 'Description', 'Support Remarks']
    fieldvalues = ['id', 'type', 'description', 'supportremarks']
    fieldids = ['id', 'type', 'description', 'supportremarks']
    tableid = modifier.addTableForModel('oss', 'componenttype', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
