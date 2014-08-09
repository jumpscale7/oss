[rootmodel:organization] @index
    """
    organization is e.g. a company or department in company
    """
    prop:name str,,domain
    prop:id int,,
    prop:description str,,
    prop:companyname str,,optional name for e.g. a com
    prop:parent int,,organization can belong to other organization
    prop:parent_name str,,
    prop:addresses list(address),,
    prop:contacts list(contact),,
    prop:vatnr str,,
    prop:datasources list(datasource),,source(s) where data comes from
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[model:address]
    prop:id int,,
    prop:country str,,
    prop:city str,,
    prop:citycode str,,
    prop:street str,,
    prop:nr int,,

[model:contact]
    prop:id int,,
    prop:type str,, {phone;mobile;email;skype}
    prop:value str,,e.g. tel nr

[rootmodel:user] @index
    """
    users
    """
    prop:id int,,    
    prop:organization str,,
    prop:name str,,
    prop:addresses list(address),,
    prop:comments list(comment),,
    prop:contacts list(contact),,
    prop:datasources list(datasource),,source(s) where data comes from
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)

[rootmodel:group] @index
    """
    group of users
    """
    prop:id int,,    
    prop:name str,,
    prop:members list(int),,users in group (based on ids)
    prop:members_name list(str),,
    prop:comments list(comment),,
    prop:contacts list(contact),,
    prop:datasources list(datasource),,source(s) where data comes from
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)

[rootmodel:ticket] @index
    """
    supported types:story;task;issue;event;bug;feature;ticket;perfissue,check
    """
    prop:id int,,    
    prop:name str,,
    prop:description str,,
    prop:priority int,,level 0-4 (4 is most urgent)
    prop:project int,,link to project
    prop:project_name str,,
    prop:type str,,supported types:story;task;issue;event;bug;feature;ticket;perfissue,check
    prop:parent int,,
    prop:parent_name str,,
    prop:depends list(int),,this task depends on
    prop:depends_names list(str),,
    prop:deadline int,,epoch of when task needs to be done
    prop:duplicate list(int),,list of duplicates to this issue
    prop:duplicate_names list(str),,
    prop:taskowner int,,owner of task (user)
    prop:taskowner_name str,,owner of task (user)
    prop:source int,,owner of task (user)
    prop:source_name str,,name of user where request came from (can be email, username, ...)   
    prop:sprint int,,
    prop:sprint_name str,,
    prop:organization int,, link to organization if any
    prop:organization_name str,,
    prop:nextstep int,,date for next day to continue with this ticket
    prop:workflow_name str,,current workflow active
    prop:job_status str,,values are: PENDING,ACTIVE,ERROR,OK,WARNING,CRITICAL
    prop:jobs list(int),,link to workflows
    prop:time_created int,,
    prop:time_lastmessage int,,
    prop:time_lastresponse int,,
    prop:time_closed int,,
    prop:messages list(message),, 
    prop:comments list(comment),,
    prop:datasources list(datasource),,source(s) where data comes from
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:params str,,json representation of dict which has all arguments required for this ticket

[model:comment]
    """
    """
    prop:comment str,,
    prop:time int,,epoch
    prop:author int,, who created comment
    prop:author_name str,, who created comment

[rootmodel:message] @index
    """
    """
    prop:id int,,    
    prop:subject str,,
    prop:message str,,
    prop:destination list(str),,
    prop:time int,,epoch
    prop:type str,,types are: email;sms;gtalk;tel
    prop:ticket int,,

[model:datasource]
    """
    """
    prop:name str,,
    prop:id int,,


[rootmodel:workflow] @index
    """
    project
    """
    prop:id int,,    
    prop:name str,,
    prop:tickettype str,,supported types:story;task;issue;event;bug;feature;ticket;perfissue,check (if empty then all)
    prop:description str,,
    prop:steps list(workflow_step),,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)

[model:workflow_step]
    """
    project
    """
    prop:name str,,
    prop:description str,,
    prop:warningtime int,, time that this step can take till warning (in sec)
    prop:criticaltime int,, time that this step can take
    prop:nextsteps list(str),,
    prop:nextsteps_error list(str),,
    prop:jscript str,,

[rootmodel:job] @index
    """
    project
    """
    prop:id int,,  
    prop:name str,,  
    prop:startdate int,,
    prop:enddate int,,
    prop:status str,,values are: PENDING,ACTIVE,ERROR,OK,WARNING,CRITICAL
    prop:steps list(workflow_step),,
    prop:steps list(job_step),,    
    prop:jobid int,,
    
[model:job_step]
    """
    project
    """
    prop:name str,,
    prop:params str,,json representation of dict which has all arguments    
    prop:warningtime int,, time that this step can take till warning (in sec)
    prop:criticaltime int,, time that this step can take
    prop:startdate int,,
    prop:enddate int,,
    prop:status str,,values are: PENDING,ACTIVE,ERROR,OK,WARNING,CRITICAL
    prop:nextstep str,,
    prop:logs str,,

[rootmodel:project] @index
    """
    project
    """
    prop:id int,,    
    prop:name str,,
    prop:descr str,,
    prop:organizations list(int),,which organizations is proj linked to
    prop:organizations_names str,,comma separated list of names of orgs
    prop:deadline int,,epoch of when task needs to be done
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:sprint] @index
    """
    """
    prop:id int,,    
    prop:name str,,
    prop:description str,,
    prop:start int,,epoch
    prop:stop int,,epoch
    prop:organizations list(int),,organizations involved with this sprint
    prop:organizations_names str,,comma separated list of names of orgs
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:datacenter] @index
    """
    """
    prop:id int,,  
    prop:name str,,
    prop:label str,,  
    prop:organization int,,id of organization which owns dc
    prop:organization_name str,,
    prop:description str,,
    prop:addresses list(address),,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:pod] @index
    """
    is group of racks (can be a row or any group)
    """
    prop:id int,,  
    prop:name str,,  
    prop:label str,,     
    prop:organization int,,id of organization which owns the pod if any
    prop:organization_name str,,
    prop:datacenter int,,
    prop:datacenter_name str,,
    prop:description str,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:rack] @index
    """
    """
    prop:id int,,    
    prop:name str,,  
    prop:label str,,      
    prop:pod int,,
    prop:pod_name str,,    
    prop:datacenter int,,
    prop:datacenter_name str,,
    prop:organization int,,id of organization which owns the rack if any
    prop:organization_name str,,
    prop:description str,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:machine] @index
    """
    """
    prop:id int,,
    prop:name str,,
    prop:organization int,,id of organization which owns the machine if any
    prop:organization_name str,,
    prop:label str,,
    prop:parent int,,
    prop:parent_name str,,
    prop:description str,,
    prop:type str,,
    prop:interfaces list(interface),,
    prop:depends list(int),, link to other machines (what does it need to work)
    prop:depends_names list(str),,
    prop:assethost int,,who is asset hosting this machine
    prop:memory int,,in GB
    prop:ssdcapacity int,,in GB
    prop:hdcapacity int,,in GB
    prop:cpumhz int,,in mhz
    prop:nrcores int,,
    prop:nrcpu int,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[rootmodel:asset] @index
    """
    """
    prop:id int,,
    prop:organization int,,id of organization which owns the asset if any
    prop:organization_names str,,comma separated list of name
    prop:label str,,
    prop:parent int,,
    prop:parent_name str,,
    prop:description str,,
    prop:type str,,
    prop:brand str,,
    prop:model str,,
    prop:interfaces list(interface),,
    prop:components list(component),,
    prop:depends list(int),, link to other assets (what does it need to work)
    prop:depends_names list(str),,
    prop:rackid int,,
    prop:datacenter_name str,,
    prop:pod_name str,,
    prop:rack_name str,,
    prop:datacenter_label str,,
    prop:pod_label str,,
    prop:rack_label str,,
    prop:U int,,how many U taken
    prop:rackpos int,, how many U starting from bottomn
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(comment),,

[model:component] @index
    """
    """
    prop:type str,,
    prop:nr int,,amount of component e.g. 2 CPU
    prop:brand str,,
    prop:model str,,
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(comment),,

[rootmodel:interface] @index
    """
    """
    prop:type str,,
    prop:macaddr str,,
    prop:vlanid str,,
    prop:vxlanid str,,
    prop:organization int,,id of organization which owns the ipaddr if any
    prop:netaddr list(netaddr),, 
    prop:connects list(int),, link to other interfaces
    prop:brand str,,
    prop:model str,,
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(comment),,

[rootmodel:netaddr] @index
    """
    """
    prop:id int,,
    prop:ipaddr str,, e.g. 192.168.10.1/24
    prop:ipaddr6 str,, 
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(comment),,

[rootmodel:componenttype] @index
    """
    examples nic,processor
    """
    prop:type str,,
    prop:description str,,
    prop:supportremarks str,,

[rootmodel:brandtype] @index
    """
    examples dell, hp, ...
    """
    prop:type str,,
    prop:description str,,
    prop:supportremarks str,,

[rootmodel:assettype] @index
    """
    examples server,ups,pdu, ...
    """
    prop:type str,,
    prop:description str,,
    prop:supportremarks str,,

[rootmodel:interfacetype] @index
    """
    """
    prop:type str,,
    prop:description str,,
    prop:supportremarks str,,

    

    