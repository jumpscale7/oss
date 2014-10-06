def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing project id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    project = ossclient.project.simpleSearch({'id':int(id)})

    if not project:
        params.result = ('Project with id %s not found' % id, args.doc)
        return params

    project = project[0]
    
    project['organizations'] = ' ,'.join(project['organizations'])
    project['deadline'] = j.base.time.epoch2HRDate(project['deadline'])

    for comment in project['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    
    args.doc.applyTemplate(project)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True