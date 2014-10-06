
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Label', 'Organization', 'Datacenter', 'Description']
    fieldvalues = ['[%(id)s|/oss/pod?id=%(id)s]', "name", 'label', 'organization_name', 'datacenter_name', 'description']
    fieldids = ['id', "name", 'label', 'organization_name', 'datacenter_name', 'description']
    tableid = modifier.addTableForModel('oss', 'pod', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
