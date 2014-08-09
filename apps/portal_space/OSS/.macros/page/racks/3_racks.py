
def main(j, args, params, tags, tasklet):
    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Name', 'Label', 'Datacenter', 'Organization', 'Description']
    fieldvalues = ['id', 'name','label', 'datacenter_name', '[%(organization_name)s|/oss/organization?id=%(organization)s]', 'description']
    fieldids = ['id', 'name', 'label', 'datacenter_name', 'organization_name', 'description']
    tableid = modifier.addTableForModel('oss', 'rack', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
