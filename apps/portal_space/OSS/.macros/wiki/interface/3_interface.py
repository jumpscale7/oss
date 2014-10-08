def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing interface id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    interface = ossclient.interface.simpleSearch({'id':int(id)})

    if not interface:
        params.result = ('Interface with id %s not found' % id, args.doc)
        return params

    interface = interface[0]
    
    org = ossclient.organization.simpleSearch({'id': interface['organization']})
    if not org:
        org = [{'id':None, 'name':'N/A'}]
    interface['organization'] = {'id': interface['organization'], 'name': org[0]['name']}
    for comment in interface['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])
    args.doc.applyTemplate(interface)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True