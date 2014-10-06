def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing pod id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    pod = ossclient.pod.simpleSearch({'id':int(id)})

    if not pod:
        params.result = ('Pod with id %s not found' % id, args.doc)
        return params

    pod = pod[0]


    args.doc.applyTemplate(pod)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True