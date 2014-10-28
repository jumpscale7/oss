from JumpScale import j

class oss_workflowstep_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    project
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_name=""
    
        self._P_description=""
    
        self._P_warningtime=0
    
        self._P_criticaltime=0
    
        self._P_nextsteps=dict()
    
        self._P_nextsteps_error=dict()
    
        self._P_jscript=""
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","workflowstep",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
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
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def warningtime(self):
        return self._P_warningtime
    @warningtime.setter
    def warningtime(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property warningtime input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
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
                msg="property criticaltime input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_criticaltime=value
    @criticaltime.deleter
    def criticaltime(self):
        del self._P_criticaltime


    @property
    def nextsteps(self):
        return self._P_nextsteps
    @nextsteps.setter
    def nextsteps(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property nextsteps input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nextsteps=value
    @nextsteps.deleter
    def nextsteps(self):
        del self._P_nextsteps


    @property
    def nextsteps_error(self):
        return self._P_nextsteps_error
    @nextsteps_error.setter
    def nextsteps_error(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property nextsteps_error input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nextsteps_error=value
    @nextsteps_error.deleter
    def nextsteps_error(self):
        del self._P_nextsteps_error


    @property
    def jscript(self):
        return self._P_jscript
    @jscript.setter
    def jscript(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property jscript input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_jscript=value
    @jscript.deleter
    def jscript(self):
        del self._P_jscript


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comments=value
    @comments.deleter
    def comments(self):
        del self._P_comments


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflowstep, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

