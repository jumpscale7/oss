from JumpScale import j

class oss_workflow_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    project
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_name=""
    
        self._P_tickettype=""
    
        self._P_description=""
    
        self._P_steps=list()
    
        self._P_acl=dict()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","workflow",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def tickettype(self):
        return self._P_tickettype
    @tickettype.setter
    def tickettype(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property tickettype input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_tickettype=value
    @tickettype.deleter
    def tickettype(self):
        del self._P_tickettype


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def steps(self):
        return self._P_steps
    @steps.setter
    def steps(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property steps input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_steps=value
    @steps.deleter
    def steps(self):
        del self._P_steps


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_acl=value
    @acl.deleter
    def acl(self):
        del self._P_acl


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: workflow, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta


    def new_step(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","workflow_step")()
        else:
            value2=value
        
        self._P_steps.append(value2)
        if self._P_steps[-1].__dict__.has_key("_P_id"):
            self._P_steps[-1].id=len(self._P_steps)
        return self._P_steps[-1]
        
    
