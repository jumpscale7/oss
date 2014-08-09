
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    filters = dict()
    for tag, val in args.tags.tags.iteritems():
        val = args.getTag(tag)
        if j.basetype.integer.checkString(val):
            val = int(val)
        filters[tag] = val

    fieldnames = ['ID', 'Organization', 'Label', 'Type', 'Description']
    fieldvalues = ['[%(id)s|/oss/machine?id=%(id)s]', 'organization', 'label', 'type', 'description']
    fieldids = ['id',  'organization', 'label', 'type', 'description']
    tableid = modifier.addTableForModel('oss', 'machine', fieldids, fieldnames, fieldvalues, filters=filters)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
