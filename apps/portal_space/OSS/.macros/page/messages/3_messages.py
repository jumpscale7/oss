
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    fieldnames = ['ID', 'Subject', 'Time']
    fieldvalues = ['[%(id)s|/oss/message?id=%(id)s]', 'subject', modifier.makeTime]
    fieldids = ['id', 'subject', "time"]
    tableid = modifier.addTableForModel('oss', 'message', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
