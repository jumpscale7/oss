def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing user id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    user = ossclient.user.simpleSearch({'id':int(id)})

    if not user:
        params.result = ('user with id %s not found' % id, args.doc)
        return params

    user = user[0]

    for comment in user['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    
    args.doc.applyTemplate(user)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True