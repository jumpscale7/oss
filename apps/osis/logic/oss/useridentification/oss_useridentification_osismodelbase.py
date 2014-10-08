from JumpScale import j

class oss_useridentification_osismodelbase(j.code.classGetJSRootModelBase()):
    """
    usersid e.g. passport
    
    """
    def __init__(self):
        self._P_userid=0
    
        self._P_type=""
    
        self._P_identificationnr=""
    
        self._P_registrationdate=0
    
        self._P_expirationdate=0
    
        self._P_description=""
    
        self._P_status=""
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","useridentification",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def userid(self):
        return self._P_userid
    @userid.setter
    def userid(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property userid input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_userid=value
    @userid.deleter
    def userid(self):
        del self._P_userid


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def identificationnr(self):
        return self._P_identificationnr
    @identificationnr.setter
    def identificationnr(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property identificationnr input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_identificationnr=value
    @identificationnr.deleter
    def identificationnr(self):
        del self._P_identificationnr


    @property
    def registrationdate(self):
        return self._P_registrationdate
    @registrationdate.setter
    def registrationdate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property registrationdate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_registrationdate=value
    @registrationdate.deleter
    def registrationdate(self):
        del self._P_registrationdate


    @property
    def expirationdate(self):
        return self._P_expirationdate
    @expirationdate.setter
    def expirationdate(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property expirationdate input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_expirationdate=value
    @expirationdate.deleter
    def expirationdate(self):
        del self._P_expirationdate


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def status(self):
        return self._P_status
    @status.setter
    def status(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property status input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_status=value
    @status.deleter
    def status(self):
        del self._P_status


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: useridentification, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

