
def main(j, args, params, tags, tasklet):

    page = args.page
    modifier = j.html.getPageModifierGridDataTables(page)

    def makedate(row, field):
        return j.base.time.epoch2HRDate(row[field])

    fieldnames = ['ID', 'Name', 'Start Date', 'End Date', 'Status']
    fieldvalues = ['[%(id)s|/oss/job?id=%(id)s]', "name", makedate, makedate, 'status']
    fieldids = ['id', "name", 'startdate', 'enddate', 'status']
    tableid = modifier.addTableForModel('oss', 'job', fieldids, fieldnames, fieldvalues)
    modifier.addSearchOptions('#%s' % tableid)

    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
