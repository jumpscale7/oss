from JumpScale import j

class oss_service_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_id=0
    
        self._P_name=""
    
        self._P_organization=""
    
        self._P_organization_name=""
    
        self._P_label=""
    
        self._P_parent=0
    
        self._P_parent_name=""
    
        self._P_description=""
    
        self._P_type=""
    
        self._P_serviceports=list()
    
        self._P_depends=list()
    
        self._P_depends_names=list()
    
        self._P_machinehost=0
    
        self._P_memory=0
    
        self._P_ssdcapacity=0
    
        self._P_hdcapacity=0
    
        self._P_cpumhz=0
    
        self._P_nrcores=0
    
        self._P_nrcpu=0
    
        self._P_admin_name=""
    
        self._P_admin_passwd=""
    
        self._P_acl=dict()
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","service",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
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
                msg="property name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_name=value
    @name.deleter
    def name(self):
        del self._P_name


    @property
    def organization(self):
        return self._P_organization
    @organization.setter
    def organization(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property organization input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization=value
    @organization.deleter
    def organization(self):
        del self._P_organization


    @property
    def organization_name(self):
        return self._P_organization_name
    @organization_name.setter
    def organization_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property organization_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization_name=value
    @organization_name.deleter
    def organization_name(self):
        del self._P_organization_name


    @property
    def label(self):
        return self._P_label
    @label.setter
    def label(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property label input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_label=value
    @label.deleter
    def label(self):
        del self._P_label


    @property
    def parent(self):
        return self._P_parent
    @parent.setter
    def parent(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property parent input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
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
                msg="property parent_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_parent_name=value
    @parent_name.deleter
    def parent_name(self):
        del self._P_parent_name


    @property
    def description(self):
        return self._P_description
    @description.setter
    def description(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_description=value
    @description.deleter
    def description(self):
        del self._P_description


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def serviceports(self):
        return self._P_serviceports
    @serviceports.setter
    def serviceports(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property serviceports input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_serviceports=value
    @serviceports.deleter
    def serviceports(self):
        del self._P_serviceports


    @property
    def depends(self):
        return self._P_depends
    @depends.setter
    def depends(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property depends input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_depends=value
    @depends.deleter
    def depends(self):
        del self._P_depends


    @property
    def depends_names(self):
        return self._P_depends_names
    @depends_names.setter
    def depends_names(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property depends_names input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_depends_names=value
    @depends_names.deleter
    def depends_names(self):
        del self._P_depends_names


    @property
    def machinehost(self):
        return self._P_machinehost
    @machinehost.setter
    def machinehost(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property machinehost input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_machinehost=value
    @machinehost.deleter
    def machinehost(self):
        del self._P_machinehost


    @property
    def memory(self):
        return self._P_memory
    @memory.setter
    def memory(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property memory input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_memory=value
    @memory.deleter
    def memory(self):
        del self._P_memory


    @property
    def ssdcapacity(self):
        return self._P_ssdcapacity
    @ssdcapacity.setter
    def ssdcapacity(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property ssdcapacity input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ssdcapacity=value
    @ssdcapacity.deleter
    def ssdcapacity(self):
        del self._P_ssdcapacity


    @property
    def hdcapacity(self):
        return self._P_hdcapacity
    @hdcapacity.setter
    def hdcapacity(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property hdcapacity input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_hdcapacity=value
    @hdcapacity.deleter
    def hdcapacity(self):
        del self._P_hdcapacity


    @property
    def cpumhz(self):
        return self._P_cpumhz
    @cpumhz.setter
    def cpumhz(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property cpumhz input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_cpumhz=value
    @cpumhz.deleter
    def cpumhz(self):
        del self._P_cpumhz


    @property
    def nrcores(self):
        return self._P_nrcores
    @nrcores.setter
    def nrcores(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property nrcores input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nrcores=value
    @nrcores.deleter
    def nrcores(self):
        del self._P_nrcores


    @property
    def nrcpu(self):
        return self._P_nrcpu
    @nrcpu.setter
    def nrcpu(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property nrcpu input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_nrcpu=value
    @nrcpu.deleter
    def nrcpu(self):
        del self._P_nrcpu


    @property
    def admin_name(self):
        return self._P_admin_name
    @admin_name.setter
    def admin_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property admin_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_admin_name=value
    @admin_name.deleter
    def admin_name(self):
        del self._P_admin_name


    @property
    def admin_passwd(self):
        return self._P_admin_passwd
    @admin_passwd.setter
    def admin_passwd(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property admin_passwd input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_admin_passwd=value
    @admin_passwd.deleter
    def admin_passwd(self):
        del self._P_admin_passwd


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
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
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: service, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

