
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'IP Address', 'IPv6 Address', 'Description']
    fieldvalues = ['[%(id)s|/oss/netaddr?id=%(id)s]', 'ipaddr', 'ipaddr6','description']
    fieldids = ['id', 'ipaddr', 'ipaddr6', 'description']
    tableid = modifier.addTableForModel('oss', 'netaddr', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
