from JumpScale import j

class oss_netaddr_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_id=0
    
        self._P_ipaddr=""
    
        self._P_ipaddr6=""
    
        self._P_description=""
    
        self._P_supportremarks=""
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","netaddr",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def ipaddr(self):
        return self._P_ipaddr
    @ipaddr.setter
    def ipaddr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ipaddr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ipaddr=value
    @ipaddr.deleter
    def ipaddr(self):
        del self._P_ipaddr


    @property
    def ipaddr6(self):
        return self._P_ipaddr6
    @ipaddr6.setter
    def ipaddr6(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ipaddr6 input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ipaddr6=value
    @ipaddr6.deleter
    def ipaddr6(self):
        del self._P_ipaddr6


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def supportremarks(self):
        return self._P_supportremarks
    @supportremarks.setter
    def supportremarks(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property supportremarks input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_supportremarks=value
    @supportremarks.deleter
    def supportremarks(self):
        del self._P_supportremarks


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: netaddr, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta


    def new_comment(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","comment")()
        else:
            value2=value
        
        self._P_comments.append(value2)
        if self._P_comments[-1].__dict__.has_key("_P_id"):
            self._P_comments[-1].id=len(self._P_comments)
        return self._P_comments[-1]
        
    
