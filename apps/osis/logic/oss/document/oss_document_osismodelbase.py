from JumpScale import j

class oss_document_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_id=0
    
        self._P_parent=0
    
        self._P_name=""
    
        self._P_creationdate=0
    
        self._P_moddate=0
    
        self._P_type=""
    
        self._P_ext=""
    
        self._P_contents=""
    
        self._P_objstorid=""
    
        self._P_description=""
    
        self._P_acl=dict()
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","document",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def parent(self):
        return self._P_parent
    @parent.setter
    def parent(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property parent input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_parent=value
    @parent.deleter
    def parent(self):
        del self._P_parent


    @property
    def name(self):
        return self._P_name
    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def creationdate(self):
        return self._P_creationdate
    @creationdate.setter
    def creationdate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property creationdate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_creationdate=value
    @creationdate.deleter
    def creationdate(self):
        del self._P_creationdate


    @property
    def moddate(self):
        return self._P_moddate
    @moddate.setter
    def moddate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property moddate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_moddate=value
    @moddate.deleter
    def moddate(self):
        del self._P_moddate


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def ext(self):
        return self._P_ext
    @ext.setter
    def ext(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property ext input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ext=value
    @ext.deleter
    def ext(self):
        del self._P_ext


    @property
    def contents(self):
        return self._P_contents
    @contents.setter
    def contents(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property contents input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_contents=value
    @contents.deleter
    def contents(self):
        del self._P_contents


    @property
    def objstorid(self):
        return self._P_objstorid
    @objstorid.setter
    def objstorid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property objstorid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_objstorid=value
    @objstorid.deleter
    def objstorid(self):
        del self._P_objstorid


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
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
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: document, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

