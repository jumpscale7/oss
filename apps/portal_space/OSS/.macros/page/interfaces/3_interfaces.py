
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Type', 'MAC Address', 'VLAN ID', 'Description']
    fieldvalues = ['[%(id)s|/oss/interface?id=%(id)s]', 'type', 'macaddr', 'vlanid', 'description']
    fieldids = ['id', 'type', 'macaddr', 'vlanid', 'description']
    tableid = modifier.addTableForModel('oss', 'interface', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
