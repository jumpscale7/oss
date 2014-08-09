from JumpScale import j

class oss_interface_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_type=""
    
        self._P_macaddr=""
    
        self._P_vlanid=""
    
        self._P_vxlanid=""
    
        self._P_organization=0
    
        self._P_netaddr=list()
    
        self._P_connects=list()
    
        self._P_brand=""
    
        self._P_model=""
    
        self._P_description=""
    
        self._P_supportremarks=""
    
        self._P_comments=list()
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","interface",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def macaddr(self):
        return self._P_macaddr
    @macaddr.setter
    def macaddr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property macaddr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_macaddr=value
    @macaddr.deleter
    def macaddr(self):
        del self._P_macaddr


    @property
    def vlanid(self):
        return self._P_vlanid
    @vlanid.setter
    def vlanid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property vlanid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_vlanid=value
    @vlanid.deleter
    def vlanid(self):
        del self._P_vlanid


    @property
    def vxlanid(self):
        return self._P_vxlanid
    @vxlanid.setter
    def vxlanid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property vxlanid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_vxlanid=value
    @vxlanid.deleter
    def vxlanid(self):
        del self._P_vxlanid


    @property
    def organization(self):
        return self._P_organization
    @organization.setter
    def organization(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property organization input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization=value
    @organization.deleter
    def organization(self):
        del self._P_organization


    @property
    def netaddr(self):
        return self._P_netaddr
    @netaddr.setter
    def netaddr(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property netaddr input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_netaddr=value
    @netaddr.deleter
    def netaddr(self):
        del self._P_netaddr


    @property
    def connects(self):
        return self._P_connects
    @connects.setter
    def connects(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property connects input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_connects=value
    @connects.deleter
    def connects(self):
        del self._P_connects


    @property
    def brand(self):
        return self._P_brand
    @brand.setter
    def brand(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property brand input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_brand=value
    @brand.deleter
    def brand(self):
        del self._P_brand


    @property
    def model(self):
        return self._P_model
    @model.setter
    def model(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property model input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_model=value
    @model.deleter
    def model(self):
        del self._P_model


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
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
                msg="property supportremarks input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
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
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comments=value
    @comments.deleter
    def comments(self):
        del self._P_comments


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: interface, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta


    def new_netaddr(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","netaddr")()
        else:
            value2=value
        
        self._P_netaddr.append(value2)
        if self._P_netaddr[-1].__dict__.has_key("_P_id"):
            self._P_netaddr[-1].id=len(self._P_netaddr)
        return self._P_netaddr[-1]
        
    

    def new_comment(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","comment")()
        else:
            value2=value
        
        self._P_comments.append(value2)
        if self._P_comments[-1].__dict__.has_key("_P_id"):
            self._P_comments[-1].id=len(self._P_comments)
        return self._P_comments[-1]
        
    
