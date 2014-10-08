from JumpScale import j

class oss_ticket_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    supported types:story;task;issue;event;bug;feature;ticket;perfissue,check
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_name=""
    
        self._P_description=""
    
        self._P_priority=0
    
        self._P_project=0
    
        self._P_project_name=""
    
        self._P_type=""
    
        self._P_parent=0
    
        self._P_parent_name=""
    
        self._P_depends=list()
    
        self._P_depends_names=list()
    
        self._P_deadline=0
    
        self._P_duplicate=list()
    
        self._P_duplicate_names=list()
    
        self._P_taskowner=0
    
        self._P_taskowner_name=""
    
        self._P_source=0
    
        self._P_source_name=""
    
        self._P_sprint=0
    
        self._P_sprint_name=""
    
        self._P_organization=0
    
        self._P_organization_name=""
    
        self._P_nextstep=0
    
        self._P_workflow_name=""
    
        self._P_job_status=""
    
        self._P_jobs=list()
    
        self._P_time_created=0
    
        self._P_time_lastmessage=0
    
        self._P_time_lastresponse=0
    
        self._P_time_closed=0
    
        self._P_messages=list()
    
        self._P_comments=list()
    
        self._P_datasources=list()
    
        self._P_acl=dict()
    
        self._P_params=""
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","ticket",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def name(self):
        return self._P_name
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def priority(self):
        return self._P_priority
    @priority.setter
    def priority(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property priority input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_priority=value
    @priority.deleter
    def priority(self):
        del self._P_priority


    @property
    def project(self):
        return self._P_project
    @project.setter
    def project(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property project input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_project=value
    @project.deleter
    def project(self):
        del self._P_project


    @property
    def project_name(self):
        return self._P_project_name
    @project_name.setter
    def project_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property project_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_project_name=value
    @project_name.deleter
    def project_name(self):
        del self._P_project_name


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def parent(self):
        return self._P_parent
    @parent.setter
    def parent(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property parent input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_parent=value
    @parent.deleter
    def parent(self):
        del self._P_parent


    @property
    def parent_name(self):
        return self._P_parent_name
    @parent_name.setter
    def parent_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property parent_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_parent_name=value
    @parent_name.deleter
    def parent_name(self):
        del self._P_parent_name


    @property
    def depends(self):
        return self._P_depends
    @depends.setter
    def depends(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property depends input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_depends=value
    @depends.deleter
    def depends(self):
        del self._P_depends


    @property
    def depends_names(self):
        return self._P_depends_names
    @depends_names.setter
    def depends_names(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property depends_names input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_depends_names=value
    @depends_names.deleter
    def depends_names(self):
        del self._P_depends_names


    @property
    def deadline(self):
        return self._P_deadline
    @deadline.setter
    def deadline(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property deadline input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_deadline=value
    @deadline.deleter
    def deadline(self):
        del self._P_deadline


    @property
    def duplicate(self):
        return self._P_duplicate
    @duplicate.setter
    def duplicate(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property duplicate input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_duplicate=value
    @duplicate.deleter
    def duplicate(self):
        del self._P_duplicate


    @property
    def duplicate_names(self):
        return self._P_duplicate_names
    @duplicate_names.setter
    def duplicate_names(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property duplicate_names input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_duplicate_names=value
    @duplicate_names.deleter
    def duplicate_names(self):
        del self._P_duplicate_names


    @property
    def taskowner(self):
        return self._P_taskowner
    @taskowner.setter
    def taskowner(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property taskowner input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_taskowner=value
    @taskowner.deleter
    def taskowner(self):
        del self._P_taskowner


    @property
    def taskowner_name(self):
        return self._P_taskowner_name
    @taskowner_name.setter
    def taskowner_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property taskowner_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_taskowner_name=value
    @taskowner_name.deleter
    def taskowner_name(self):
        del self._P_taskowner_name


    @property
    def source(self):
        return self._P_source
    @source.setter
    def source(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property source input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_source=value
    @source.deleter
    def source(self):
        del self._P_source


    @property
    def source_name(self):
        return self._P_source_name
    @source_name.setter
    def source_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property source_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_source_name=value
    @source_name.deleter
    def source_name(self):
        del self._P_source_name


    @property
    def sprint(self):
        return self._P_sprint
    @sprint.setter
    def sprint(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property sprint input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_sprint=value
    @sprint.deleter
    def sprint(self):
        del self._P_sprint


    @property
    def sprint_name(self):
        return self._P_sprint_name
    @sprint_name.setter
    def sprint_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property sprint_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_sprint_name=value
    @sprint_name.deleter
    def sprint_name(self):
        del self._P_sprint_name


    @property
    def organization(self):
        return self._P_organization
    @organization.setter
    def organization(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property organization input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization=value
    @organization.deleter
    def organization(self):
        del self._P_organization


    @property
    def organization_name(self):
        return self._P_organization_name
    @organization_name.setter
    def organization_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property organization_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization_name=value
    @organization_name.deleter
    def organization_name(self):
        del self._P_organization_name


    @property
    def nextstep(self):
        return self._P_nextstep
    @nextstep.setter
    def nextstep(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property nextstep input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nextstep=value
    @nextstep.deleter
    def nextstep(self):
        del self._P_nextstep


    @property
    def workflow_name(self):
        return self._P_workflow_name
    @workflow_name.setter
    def workflow_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property workflow_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_workflow_name=value
    @workflow_name.deleter
    def workflow_name(self):
        del self._P_workflow_name


    @property
    def job_status(self):
        return self._P_job_status
    @job_status.setter
    def job_status(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property job_status input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_job_status=value
    @job_status.deleter
    def job_status(self):
        del self._P_job_status


    @property
    def jobs(self):
        return self._P_jobs
    @jobs.setter
    def jobs(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property jobs input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_jobs=value
    @jobs.deleter
    def jobs(self):
        del self._P_jobs


    @property
    def time_created(self):
        return self._P_time_created
    @time_created.setter
    def time_created(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time_created input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time_created=value
    @time_created.deleter
    def time_created(self):
        del self._P_time_created


    @property
    def time_lastmessage(self):
        return self._P_time_lastmessage
    @time_lastmessage.setter
    def time_lastmessage(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time_lastmessage input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time_lastmessage=value
    @time_lastmessage.deleter
    def time_lastmessage(self):
        del self._P_time_lastmessage


    @property
    def time_lastresponse(self):
        return self._P_time_lastresponse
    @time_lastresponse.setter
    def time_lastresponse(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time_lastresponse input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time_lastresponse=value
    @time_lastresponse.deleter
    def time_lastresponse(self):
        del self._P_time_lastresponse


    @property
    def time_closed(self):
        return self._P_time_closed
    @time_closed.setter
    def time_closed(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time_closed input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time_closed=value
    @time_closed.deleter
    def time_closed(self):
        del self._P_time_closed


    @property
    def messages(self):
        return self._P_messages
    @messages.setter
    def messages(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property messages input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_messages=value
    @messages.deleter
    def messages(self):
        del self._P_messages


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comments=value
    @comments.deleter
    def comments(self):
        del self._P_comments


    @property
    def datasources(self):
        return self._P_datasources
    @datasources.setter
    def datasources(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property datasources input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_datasources=value
    @datasources.deleter
    def datasources(self):
        del self._P_datasources


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_acl=value
    @acl.deleter
    def acl(self):
        del self._P_acl


    @property
    def params(self):
        return self._P_params
    @params.setter
    def params(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property params input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_params=value
    @params.deleter
    def params(self):
        del self._P_params


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_guid=value
    @guid.deleter
    def guid(self):
        del self._P_guid


    @property
    def _meta(self):
        return self._P__meta
    @_meta.setter
    def _meta(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: ticket, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

