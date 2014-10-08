def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing datacenter id param'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')
    datacenter = ossclient.datacenter.simpleSearch({'id':int(id)})

    if not datacenter:
        params.result = ('datacenter with id %s not found' % id, args.doc)
        return params

    datacenter = datacenter[0]
    for comment in datacenter['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    args.doc.applyTemplate(datacenter)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True