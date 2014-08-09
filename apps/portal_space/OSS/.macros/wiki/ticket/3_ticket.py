def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing ticket id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    ticket = ossclient.ticket.simpleSearch({'id':int(id)})

    if not ticket:
        params.result = ('ticket with id %s not found' % id, args.doc)
        return params

    ticket = ticket[0]


    ticket['deadline'] = j.base.time.epoch2HRDate(ticket['deadline'])

    args.doc.applyTemplate(ticket)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True