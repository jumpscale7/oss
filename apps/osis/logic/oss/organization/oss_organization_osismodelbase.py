from JumpScale import j

class oss_organization_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    organization is e.g. a company or department in company
    
    """
    def __init__(self):
        self._P_name=""
    
        self._P_id=0
    
        self._P_description=""
    
        self._P_companyname=""
    
        self._P_parent=""
    
        self._P_parent_name=""
    
        self._P_addresses=list()
    
        self._P_contactmethods=list()
    
        self._P_vatnr=""
    
        self._P_datasources=list()
    
        self._P_acl=dict()
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","organization",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def name(self):
        return self._P_name
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def companyname(self):
        return self._P_companyname
    @companyname.setter
    def companyname(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property companyname input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_companyname=value
    @companyname.deleter
    def companyname(self):
        del self._P_companyname


    @property
    def parent(self):
        return self._P_parent
    @parent.setter
    def parent(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property parent input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
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
                msg="property parent_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_parent_name=value
    @parent_name.deleter
    def parent_name(self):
        del self._P_parent_name


    @property
    def addresses(self):
        return self._P_addresses
    @addresses.setter
    def addresses(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property addresses input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_addresses=value
    @addresses.deleter
    def addresses(self):
        del self._P_addresses


    @property
    def contactmethods(self):
        return self._P_contactmethods
    @contactmethods.setter
    def contactmethods(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property contactmethods input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_contactmethods=value
    @contactmethods.deleter
    def contactmethods(self):
        del self._P_contactmethods


    @property
    def vatnr(self):
        return self._P_vatnr
    @vatnr.setter
    def vatnr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property vatnr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_vatnr=value
    @vatnr.deleter
    def vatnr(self):
        del self._P_vatnr


    @property
    def datasources(self):
        return self._P_datasources
    @datasources.setter
    def datasources(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property datasources input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
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
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_acl=value
    @acl.deleter
    def acl(self):
        del self._P_acl


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: organization, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

