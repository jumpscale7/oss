def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing organization id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    organization = ossclient.organization.simpleSearch({'id':int(id)})

    if not organization:
        params.result = ('Organization with id %s not found' % id, args.doc)
        return params

    organization = organization[0]

    for comment in organization['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])

    args.doc.applyTemplate(organization)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True