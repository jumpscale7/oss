from JumpScale import j

class oss_job_step_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    project
    
    """
    def __init__(self):
        self._P_jobguid=""
    
        self._P_workflowstep_id=0
    
        self._P_workflowstep_name=""
    
        self._P_descr=""
    
        self._P_order=0
    
        self._P_params=""
    
        self._P_warningtime=0
    
        self._P_criticaltime=0
    
        self._P_startdate=0
    
        self._P_enddate=0
    
        self._P_jscript=""
    
        self._P_status=""
    
        self._P_nextsteps=list()
    
        self._P_comments=""
    
        self._P_logs=""
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","job_step",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def jobguid(self):
        return self._P_jobguid
    @jobguid.setter
    def jobguid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property jobguid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_jobguid=value
    @jobguid.deleter
    def jobguid(self):
        del self._P_jobguid


    @property
    def workflowstep_id(self):
        return self._P_workflowstep_id
    @workflowstep_id.setter
    def workflowstep_id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property workflowstep_id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_workflowstep_id=value
    @workflowstep_id.deleter
    def workflowstep_id(self):
        del self._P_workflowstep_id


    @property
    def workflowstep_name(self):
        return self._P_workflowstep_name
    @workflowstep_name.setter
    def workflowstep_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property workflowstep_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_workflowstep_name=value
    @workflowstep_name.deleter
    def workflowstep_name(self):
        del self._P_workflowstep_name


    @property
    def descr(self):
        return self._P_descr
    @descr.setter
    def descr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property descr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_descr=value
    @descr.deleter
    def descr(self):
        del self._P_descr


    @property
    def order(self):
        return self._P_order
    @order.setter
    def order(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property order input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_order=value
    @order.deleter
    def order(self):
        del self._P_order


    @property
    def params(self):
        return self._P_params
    @params.setter
    def params(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property params input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_params=value
    @params.deleter
    def params(self):
        del self._P_params


    @property
    def warningtime(self):
        return self._P_warningtime
    @warningtime.setter
    def warningtime(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property warningtime input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_warningtime=value
    @warningtime.deleter
    def warningtime(self):
        del self._P_warningtime


    @property
    def criticaltime(self):
        return self._P_criticaltime
    @criticaltime.setter
    def criticaltime(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property criticaltime input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_criticaltime=value
    @criticaltime.deleter
    def criticaltime(self):
        del self._P_criticaltime


    @property
    def startdate(self):
        return self._P_startdate
    @startdate.setter
    def startdate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property startdate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
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
                msg="property enddate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_enddate=value
    @enddate.deleter
    def enddate(self):
        del self._P_enddate


    @property
    def jscript(self):
        return self._P_jscript
    @jscript.setter
    def jscript(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property jscript input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_jscript=value
    @jscript.deleter
    def jscript(self):
        del self._P_jscript


    @property
    def status(self):
        return self._P_status
    @status.setter
    def status(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property status input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_status=value
    @status.deleter
    def status(self):
        del self._P_status


    @property
    def nextsteps(self):
        return self._P_nextsteps
    @nextsteps.setter
    def nextsteps(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property nextsteps input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nextsteps=value
    @nextsteps.deleter
    def nextsteps(self):
        del self._P_nextsteps


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property comments input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comments=value
    @comments.deleter
    def comments(self):
        del self._P_comments


    @property
    def logs(self):
        return self._P_logs
    @logs.setter
    def logs(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property logs input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_logs=value
    @logs.deleter
    def logs(self):
        del self._P_logs


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: job_step, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

