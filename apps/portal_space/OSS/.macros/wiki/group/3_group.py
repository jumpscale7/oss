def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing group id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    group = ossclient.group.simpleSearch({'id':int(id)})

    if not group:
        params.result = ('Group with id %s not found' % id, args.doc)
        return params

    group = group[0]
    
    for comment in group['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    
    args.doc.applyTemplate(group)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True