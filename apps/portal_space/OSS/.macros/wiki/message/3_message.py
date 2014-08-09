def main(j, args, params, tags, tasklet):

    id = args.getTag('id')
    if not id:
        out = 'Missing message id param "id"'
        params.result = (out, args.doc)
        return params

    ossclient = j.core.osis.getClientForNamespace('oss')

    message = ossclient.message.simpleSearch({'id':int(id)})

    if not message:
        params.result = ('Message with id %s not found' % id, args.doc)
        return params

    message = message[0]
    
    message['destination'] = ' ,'.join(message['destination'])
    message['time'] = j.base.time.epoch2HRDateTime(message['time'])

    ticket = ossclient.ticket.simpleSearch({'id': message['ticket']})
    if not ticket:
        ticket = [{'id':None, 'name':'N/A'}]
    message['ticket'] = {'id':ticket[0]['id'], 'name': ticket[0]['name']}

    user = ossclient.user.simpleSearch({'id': message['user']})
    if not user:
        user = [{'id':None, 'name':'N/A'}]
    message['user'] = {'id':user[0]['id'], 'name': user[0]['name']}
    
    args.doc.applyTemplate(message)

    params.result = (args.doc, args.doc)
    return params

def match(j, args, params, tags, tasklet):
    return True