def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing workflow id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    workflow = ossclient.workflow.simpleSearch({'id':int(id)})

    if not workflow:
        params.result = ('Workflow with id %s not found' % id, args.doc)
        return params

    workflow = workflow[0]

    for step in workflow['steps']:
        step['nextsteps'] = ', '.join(step['nextsteps'])
        step['nextsteps_error'] = ', '.join(step['nextsteps_error'])

    args.doc.applyTemplate(workflow)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True