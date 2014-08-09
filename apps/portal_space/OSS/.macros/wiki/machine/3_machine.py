def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing machine id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    machine = ossclient.machine.simpleSearch({'id':int(id)})

    if not machine:
        params.result = ('Machine with id %s not found' % id, args.doc)
        return params

    machine = machine[0]

    for comment in machine['comments']:
        comment['time'] = j.base.time.epoch2HRDateTime(comment['time'])

    args.doc.applyTemplate(machine)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True