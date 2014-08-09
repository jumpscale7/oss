def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing job id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    job = ossclient.job.simpleSearch({'id':int(id)})

    if not job:
        params.result = ('Job with id %s not found' % id, args.doc)
        return params

    job = job[0]

    job['startdate'] = j.base.time.epoch2HRDate(job['startdate'])
    job['enddate'] = j.base.time.epoch2HRDate(job['enddate'])

    for step in job['steps']:  
        step['startdate'] = j.base.time.epoch2HRDate(step['startdate'])
        step['enddate'] = j.base.time.epoch2HRDate(step['enddate'])

    args.doc.applyTemplate(job)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True