#every object has a guid
#because we are using mongodb best not to make nested structures
#every object also has an id = int they are both unique

[rootmodel:organization] @index
    """
    organization is e.g. a company or department in company
    """
    prop:name str,,domain
    prop:id int,,
    prop:description str,,
    prop:companyname str,,optional name 
    prop:parent str,,organization can belong to other organization                      @ref:organization
    prop:parent_name str,,
    prop:addresses list(str),,reference to addresses (guid)                             @ref:address
    prop:contactmethods list(str),,reference to contactmethod (guid)                    @ref:contactmethod
    prop:vatnr str,,
    prop:datasources list(str),,source(s) where data comes from (reference)             @ref:datasource
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment

[rootmodel:address]
    prop:id int,,
    prop:country str,,
    prop:city str,,
    prop:citycode str,,
    prop:zone str,,
    prop:region str,,
    prop:street str,,
    prop:nr int,,
    prop:floor int,,

[rootmodel:contactmethod]
    prop:id int,,
    prop:type str,,                                                                     @types:phone|mobile|email|skype|linkedin|facebook|jabber       
    prop:value str,,e.g. tel nr

[rootmodel:user] @index
    """
    users
    """
    prop:id int,,
    prop:list(str) str,,                                                                @ref:organization
    prop:organization_names str,,
    prop:name str,,    
    prop:addresses list(str),,reference to addr (guid)                                  @ref:addresss
    prop:comments list(str),,reference to comments                                      @ref:comment
    prop:userids list(str),,                                                            @ref:useridentification
    prop:contactmethods list(str),,reference to contactmethods                          @ref:contactmethod
    prop:datasources list(str),,source(s) where data comes from (reference)             @ref:datasource
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)

[rootmodel:useridentification] @index
    """
    usersid e.g. passport
    """
    prop:userid int,, reference to user
    prop:type str,, PASSPORT:ID:DRIVINGLICENSE
    prop:identificationnr str,,e.g. passport nr
    prop:registrationdate int,, epoch
    prop:expirationdate int,, epoch
    prop:description str,,    
    prop:status str,,VALID:EXPIRED:ERROR

[rootmodel:group] @index
    """
    group of users
    """
    prop:id int,,    
    prop:name str,,
    prop:addresses list(str),,reference to addr                                         @ref:address
    prop:members list(str),,users in group (based on ids)                               @ref:user
    prop:members_name list(str),,
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren
    prop:contactmethods list(str),,reference to contactmethods                          @ref:contactmethod
    prop:datasources list(str),,source(s) where data comes from (reference)             @ref:datasource
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)

[rootmodel:ticket] @index
    """
    supported types:story;task;issue;event;bug;feature;ticket;perfissue,check
    """
    prop:id int,,    
    prop:name str,,
    prop:description str,,
    prop:priority int,,level 0-4 (4 is most urgent)                                              @limit:0-4
    prop:project str,,link to project                                                            @ref:project
    prop:project_name str,,
    prop:type str,,                                                                              @type:story|task|issue|event|bug|feature|ticket|perfissue|check
    prop:parent str,,                                                                            @ref:ticket
    prop:parent_name str,,
    prop:depends list(str),,this task depends on                                                 @ref:ticket
    prop:depends_names list(str),,
    prop:deadline int,,epoch of when task needs to be done
    prop:duplicate list(str),,list of duplicates to this issue                                   @ref:ticket
    prop:duplicate_names list(str),,
    prop:taskowner str,,owner of task (user)                                                     @ref:user
    prop:taskowner_name str,,owner of task (user)
    prop:source str,,owner of task (user)                                                        @ref:user
    prop:source_name str,,name of user where request came from (can be email, username, ...)   
    prop:sprint str,,                                                                            @ref:user
    prop:sprint_name str,,
    prop:organization str,, link to organization if any                                          @ref:organization
    prop:organization_name str,,
    prop:nextstepdate int,,date for next day to continue with this ticket
    prop:workflow str,,current active workflow                                                   @ref:workflow
    prop:job_status str,,values are:                                                             @type:PENDING|ACTIVE|ERROR|OK|WARNING|CRITICAL
    prop:jobs list(str),,link to workflows                                                       @ref job
    prop:time_created int,,
    prop:time_lastmessage int,,
    prop:time_lastresponse int,,
    prop:time_closed int,,
    prop:messages list(str),, reference to message                                               @ref:message
    prop:comments list(str),,reference to comments                                               @ref:comment deletechildren
    prop:datasources list(str),,source(s) where data comes from (reference)                      @ref:datasource
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:params str,,json representation of dict which has all arguments required for this ticket

[rootmodel:comment]
    """
    """
    prop:comment str,,
    prop:time int,,epoch
    prop:author int,, who created comment
    prop:author_name str,, who created comment

[rootmodel:message] @index
    """
    """
    prop:subject str,,
    prop:message str,,
    prop:destination list(str),,
    prop:time int,,epoch
    prop:type str,,types are: email;sms;gtalk;tel
    prop:format str,, html;confl;md;text default is text
    prop:ticket int,,
    prop:comments list(str),,reference to comments                                               @ref:comment deletechildren

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
    prop:tickettype str,,                                                                           @type:story;task;issue;event;bug;feature;ticket;perfissue,check (if empty then all)
    prop:description str,,
    prop:workflowsteps list(str),,                                                                  @ref:workflowstep deletechildren
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                                  @ref:comment deletechildren

[rootmodel:workflowstep]
    """
    project
    """
    prop:id int,,
    prop:name str,,
    prop:description str,,
    prop:warningtime int,, time that this step can take till warning (in sec)
    prop:criticaltime int,, time that this step can take
    prop:nextsteps dict(str),,                                                                      @ref:workflowstep
    prop:nextsteps_error dict(str),,                                                                @ref:workflowstep
    prop:jscript str,,this script will create jobsteps (like branches of a tree) and return all next jobsteps to execute
    prop:comments list(str),,reference to comments                                                 @ref:comment deletechildren

[rootmodel:job] @index
    """
    project
    """
    prop:id int,,  
    prop:workflow str,,                                                                             @ref workflow
    prop:workflow_name str,,  
    prop:startdate int,,epoch
    prop:enddate int,,epoch
    prop:status str,,values are:                                                                    @type:PENDING|ACTIVE|ERROR|OK|WARNING|CRITICAL
    
[rootmodel:jobstep]
    """
    project
    """
    prop:jobguid str,,reference to job
    prop:workflow str,,                                                                             @ref workflow
    prop:workflowstep str,,reference to workflowstep which started this jobsteps                    @ref:workflowstep
    prop:workflowstep_name str,,
    prop:description str,,
    prop:order int,,order in which the steps where executed
    prop:params str,,json representation of dict which has all arguments    
    prop:warningtime int,, time that this step can take till warning (in sec)
    prop:criticaltime int,, time that this step can take
    prop:startdate int,,
    prop:enddate int,,
    prop:jscript str,,script which was executed
    prop:status str,,values are:                                                                    @type:PENDING|ACTIVE|ERROR|OK|WARNING|CRITICAL
    prop:nextsteps list(str),,after resolving the script next steps which were triggered (so is after execution), is references to other jobsteps (guid) @ref:jobstep
    prop:logs str,,

[rootmodel:project] @index
    """
    project
    """
    prop:id int,,    
    prop:name str,,
    prop:descr str,,
    prop:organizations list(str),,which organizations is proj linked to                 @ref:organization
    prop:organizations_names str,,comma separated list of names of orgs
    prop:deadline int,,epoch of when task needs to be done
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:sprint] @index
    """
    """
    prop:id int,,    
    prop:name str,,
    prop:description str,,
    prop:start int,,epoch
    prop:stop int,,epoch
    prop:organizations list(str),,organizations involved with this sprint               @ref:organization
    prop:organizations_names str,,comma separated list of names of orgs
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:datacenter] @index
    """
    """
    prop:id int,,  
    prop:name str,,
    prop:label str,,  
    prop:organization str,,id of organization which owns dc                             @ref:organization
    prop:organization_name str,,
    prop:description str,,
    prop:addresses list(str),,reference to addr                                         @ref:address
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren


[rootmodel:pod] @index
    """
    is group of racks (can be a row or any group)
    """
    prop:id int,,  
    prop:name str,,  
    prop:label str,,     
    prop:organization str,,id of organization which owns the pod if any                 @ref:organization
    prop:organization_name str,,
    prop:datacenter str,,                                                               @ref:organization
    prop:datacenter_name str,,
    prop:description str,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:rack] @index
    """
    """
    prop:id int,,    
    prop:name str,,  
    prop:label str,,      
    prop:pod str,,                                                                      @ref:pod
    prop:pod_name str,,    
    prop:datacenter str,,                                                               @ref:organization
    prop:datacenter_name str,,
    prop:organization str,,id of organization which owns the rack if any                @ref:organization
    prop:organization_name str,,
    prop:description str,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:machine] @index
    """
    """
    prop:id int,,
    prop:name str,,
    prop:organization str,,id of organization which owns the machine if any             @ref:organization
    prop:organization_name str,,
    prop:label str,,
    prop:parent int,,
    prop:parent_name str,,
    prop:description str,,
    prop:type str,,
    prop:interfaces list(str),,                                                         @ref interface
    prop:depends list(str),, link to other machines (what does it need to work)         @ref machine
    prop:depends_names list(str),,
    prop:assethost int,,who is asset hosting this machinehost                           @ref asset
    prop:memory int,,in GB
    prop:ssdcapacity int,,in GB
    prop:hdcapacity int,,in GB
    prop:cpumhz int,,in mhz
    prop:nrcores int,,
    prop:nrcpu int,,
    prop:rootpasswd str,,encrypted root passwd
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:service] @index
    """
    """
    prop:id int,,
    prop:name str,,
    prop:organization str,,id of organization which owns the service if any             @ref:organization
    prop:organization_name str,,
    prop:label str,,
    prop:parent int,,
    prop:parent_name str,,
    prop:description str,,
    prop:type str,,
    prop:serviceports list(str),,                                                       @ref:serviceport
    prop:depends list(str),, link to other services (what does it need to work)         @ref:service
    prop:depends_names list(str),,
    prop:machinehost int,,who is machine hosting this service                           @ref:host
    prop:memory int,,in GB
    prop:ssdcapacity int,,in GB
    prop:hdcapacity int,,in GB
    prop:cpumhz int,,in mhz
    prop:nrcores int,,
    prop:nrcpu int,,
    prop:admin_name str,,name of admin e.g. admin or root
    prop:admin_passwd str,,encrypted root passwd
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:serviceport] @index
    """
    there is many2many relation between services and service ports
    """
    prop:id int,,
    prop:serviceid int,,
    prop:ipaddr str,, e.g. 192.168.10.1/24
    prop:ipaddr6 str,, 
    prop:url str,,
    prop:port str,,
    prop:type str,,                                                                     @types:UDP|TCP|HTTP|HTTPS|SSH
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren


[rootmodel:asset] @index
    """
    """
    prop:id int,,
    prop:organization str,,id of organization which owns the asset if any               @ref:organization
    prop:organization_names str,,comma separated list of name
    prop:label str,,
    prop:parent str,,                                                                   @ref:asset
    prop:parent_name str,,
    prop:description str,,
    prop:type str,,
    prop:brand str,,
    prop:model str,,
    prop:interfaces list(str),,                                                         @ref:interface
    prop:components list(str),,                                                         @ref:component
    prop:depends list(str),, link to other assets (what does it need to work)           @ref:asset
    prop:depends_names list(str),,
    prop:rack str,,                                                                     @ref:rack
    prop:datacenter_name str,,
    prop:pod_name str,,
    prop:rack_name str,,
    prop:datacenter_label str,,
    prop:pod_label str,,
    prop:rack_label str,,
    prop:U int,,how many U taken
    prop:rackpos int,, how many U starting from bottomn
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:component] @index
    """
    """
    prop:type str,,
    prop:nr int,,amount of component e.g. 2 CPU
    prop:brand str,,
    prop:model str,,
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(str),,reference to comments                                  @ref:comment deletechildren

[rootmodel:interface] @index
    """
    """
    prop:type str,,
    prop:macaddr str,,
    prop:vlanid str,,
    prop:vxlanid str,,
    prop:organization str,,id of organization which owns the ipaddr if any          @ref:organization
    prop:netaddr list(str),,                                                        @ref:netaddr deletechildren
    prop:connects list(str),, link to other interfaces                              @ref:interfaces
    prop:brand str,,
    prop:model str,,
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

[rootmodel:netaddr] @index
    """
    """
    prop:id int,,
    prop:ipaddr str,, e.g. 192.168.10.1/24
    prop:ipaddr6 str,, 
    prop:description str,,
    prop:supportremarks str,,
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren

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

[rootmodel:document] @index
    """
    """
    prop:id int,,
    prop:parent int,,parent doc (where this document is a version of)
    prop:name str,,
    prop:creationdate int,,
    prop:moddate int,,
    prop:type str,, SPREADSHEET:DOC:TXT:CODE:...
    prop:ext str,, e.g. docx;xls;...
    prop:contents str,,full text content
    prop:objstorid str,,reference on doc mgmt system (stored in sort of key value obj store)
    prop:description str,,
    prop:acl dict(str),,dict where key is name of group; value is R/W/E (E=Execute)
    prop:comments list(str),,reference to comments                                      @ref:comment deletechildren


