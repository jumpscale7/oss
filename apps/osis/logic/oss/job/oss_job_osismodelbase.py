from JumpScale import j

class oss_job_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    project
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_workflow=""
    
        self._P_workflow_name=""
    
        self._P_startdate=0
    
        self._P_enddate=0
    
        self._P_status=""
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","job",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def workflow(self):
        return self._P_workflow
    @workflow.setter
    def workflow(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property workflow input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_workflow=value
    @workflow.deleter
    def workflow(self):
        del self._P_workflow


    @property
    def workflow_name(self):
        return self._P_workflow_name
    @workflow_name.setter
    def workflow_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property workflow_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_workflow_name=value
    @workflow_name.deleter
    def workflow_name(self):
        del self._P_workflow_name


    @property
    def startdate(self):
        return self._P_startdate
    @startdate.setter
    def startdate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property startdate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_startdate=value
    @startdate.deleter
    def startdate(self):
        del self._P_startdate


    @property
    def enddate(self):
        return self._P_enddate
    @enddate.setter
    def enddate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property enddate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_enddate=value
    @enddate.deleter
    def enddate(self):
        del self._P_enddate


    @property
    def status(self):
        return self._P_status
    @status.setter
    def status(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property status input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_status=value
    @status.deleter
    def status(self):
        del self._P_status


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

