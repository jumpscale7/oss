def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing sprint id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    sprint = ossclient.sprint.simpleSearch({'id':int(id)})

    if not sprint:
        params.result = ('sprint with id %s not found' % id, args.doc)
        return params

    sprint = sprint[0]

    sprint['start'] = j.base.time.epoch2HRDate(sprint['start'])
    sprint['stop'] = j.base.time.epoch2HRDate(sprint['stop'])

    for comment in sprint['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    
    args.doc.applyTemplate(sprint)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True