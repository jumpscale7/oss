from JumpScale import j

class oss_address_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_id=0
    
        self._P_country=""
    
        self._P_city=""
    
        self._P_citycode=""
    
        self._P_zone=""
    
        self._P_region=""
    
        self._P_street=""
    
        self._P_nr=0
    
        self._P_floor=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","address",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def country(self):
        return self._P_country
    @country.setter
    def country(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property country input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_country=value
    @country.deleter
    def country(self):
        del self._P_country


    @property
    def city(self):
        return self._P_city
    @city.setter
    def city(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property city input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_city=value
    @city.deleter
    def city(self):
        del self._P_city


    @property
    def citycode(self):
        return self._P_citycode
    @citycode.setter
    def citycode(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property citycode input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_citycode=value
    @citycode.deleter
    def citycode(self):
        del self._P_citycode


    @property
    def zone(self):
        return self._P_zone
    @zone.setter
    def zone(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property zone input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_zone=value
    @zone.deleter
    def zone(self):
        del self._P_zone


    @property
    def region(self):
        return self._P_region
    @region.setter
    def region(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property region input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_region=value
    @region.deleter
    def region(self):
        del self._P_region


    @property
    def street(self):
        return self._P_street
    @street.setter
    def street(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property street input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_street=value
    @street.deleter
    def street(self):
        del self._P_street


    @property
    def nr(self):
        return self._P_nr
    @nr.setter
    def nr(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property nr input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nr=value
    @nr.deleter
    def nr(self):
        del self._P_nr


    @property
    def floor(self):
        return self._P_floor
    @floor.setter
    def floor(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property floor input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_floor=value
    @floor.deleter
    def floor(self):
        del self._P_floor


    @property
    def guid(self):
        return self._P_guid
    @guid.setter
    def guid(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: address, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

