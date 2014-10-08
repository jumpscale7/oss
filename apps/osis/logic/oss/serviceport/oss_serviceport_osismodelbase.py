from JumpScale import j

class oss_serviceport_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    there is many2many relation between services and service ports
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_serviceid=0
    
        self._P_ipaddr=""
    
        self._P_ipaddr6=""
    
        self._P_url=""
    
        self._P_port=""
    
        self._P_type=""
    
        self._P_description=""
    
        self._P_supportremarks=""
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","serviceport",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def serviceid(self):
        return self._P_serviceid
    @serviceid.setter
    def serviceid(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property serviceid input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_serviceid=value
    @serviceid.deleter
    def serviceid(self):
        del self._P_serviceid


    @property
    def ipaddr(self):
        return self._P_ipaddr
    @ipaddr.setter
    def ipaddr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ipaddr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
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
                msg="property ipaddr6 input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ipaddr6=value
    @ipaddr6.deleter
    def ipaddr6(self):
        del self._P_ipaddr6


    @property
    def url(self):
        return self._P_url
    @url.setter
    def url(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property url input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_url=value
    @url.deleter
    def url(self):
        del self._P_url


    @property
    def port(self):
        return self._P_port
    @port.setter
    def port(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property port input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_port=value
    @port.deleter
    def port(self):
        del self._P_port


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
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
                msg="property supportremarks input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
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
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: serviceport, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

