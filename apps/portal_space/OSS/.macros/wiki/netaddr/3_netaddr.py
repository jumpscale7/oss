def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing netaddr id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    netaddr = ossclient.netaddr.simpleSearch({'id':int(id)})

    if not netaddr:
        params.result = ('NetAddr with id %s not found' % id, args.doc)
        return params

    netaddr = netaddr[0]

    for comment in netaddr['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    
    args.doc.applyTemplate(netaddr)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True