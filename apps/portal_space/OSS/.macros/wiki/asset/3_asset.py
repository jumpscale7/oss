def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing asset id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    asset = ossclient.asset.simpleSearch({'id':int(id)})

    if not asset:
        params.result = ('Asset with id %s not found' % id, args.doc)
        return params

    asset = asset[0]

    for comment in asset['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])

    args.doc.applyTemplate(asset)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True