from JumpScale import j

class oss_group_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    group of users
    
    """
    def __init__(self):
        self._P_id=0
    
        self._P_name=""
    
        self._P_members=list()
    
        self._P_members_name=list()
    
        self._P_comments=list()
    
        self._P_contacts=list()
    
        self._P_datasources=list()
    
        self._P_acl=dict()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","group",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def members(self):
        return self._P_members
    @members.setter
    def members(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property members input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_members=value
    @members.deleter
    def members(self):
        del self._P_members


    @property
    def members_name(self):
        return self._P_members_name
    @members_name.setter
    def members_name(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property members_name input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_members_name=value
    @members_name.deleter
    def members_name(self):
        del self._P_members_name


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comments=value
    @comments.deleter
    def comments(self):
        del self._P_comments


    @property
    def contacts(self):
        return self._P_contacts
    @contacts.setter
    def contacts(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property contacts input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_contacts=value
    @contacts.deleter
    def contacts(self):
        del self._P_contacts


    @property
    def datasources(self):
        return self._P_datasources
    @datasources.setter
    def datasources(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property datasources input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
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
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: group, value was:" + str(value)
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
        
    

    def new_contact(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","contact")()
        else:
            value2=value
        
        self._P_contacts.append(value2)
        if self._P_contacts[-1].__dict__.has_key("_P_id"):
            self._P_contacts[-1].id=len(self._P_contacts)
        return self._P_contacts[-1]
        
    

    def new_datasource(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","datasource")()
        else:
            value2=value
        
        self._P_datasources.append(value2)
        if self._P_datasources[-1].__dict__.has_key("_P_id"):
            self._P_datasources[-1].id=len(self._P_datasources)
        return self._P_datasources[-1]
        
    
