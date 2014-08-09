from JumpScale import j

class oss_asset_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_id=0
    
        self._P_organization=0
    
        self._P_organization_names=""
    
        self._P_label=""
    
        self._P_parent=0
    
        self._P_parent_name=""
    
        self._P_description=""
    
        self._P_type=""
    
        self._P_brand=""
    
        self._P_model=""
    
        self._P_interfaces=list()
    
        self._P_components=list()
    
        self._P_depends=list()
    
        self._P_depends_names=list()
    
        self._P_rackid=0
    
        self._P_datacenter_name=""
    
        self._P_pod_name=""
    
        self._P_rack_name=""
    
        self._P_datacenter_label=""
    
        self._P_pod_label=""
    
        self._P_rack_label=""
    
        self._P_U=0
    
        self._P_rackpos=0
    
        self._P_acl=dict()
    
        self._P_comments=list()
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","asset",1] #@todo version not implemented now, just already foreseen
    

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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_id=value
    @id.deleter
    def id(self):
        del self._P_id


    @property
    def organization(self):
        return self._P_organization
    @organization.setter
    def organization(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property organization input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization=value
    @organization.deleter
    def organization(self):
        del self._P_organization


    @property
    def organization_names(self):
        return self._P_organization_names
    @organization_names.setter
    def organization_names(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property organization_names input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_organization_names=value
    @organization_names.deleter
    def organization_names(self):
        del self._P_organization_names


    @property
    def label(self):
        return self._P_label
    @label.setter
    def label(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property label input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property parent input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property parent_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property description input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def brand(self):
        return self._P_brand
    @brand.setter
    def brand(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property brand input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property model input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_model=value
    @model.deleter
    def model(self):
        del self._P_model


    @property
    def interfaces(self):
        return self._P_interfaces
    @interfaces.setter
    def interfaces(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property interfaces input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_interfaces=value
    @interfaces.deleter
    def interfaces(self):
        del self._P_interfaces


    @property
    def components(self):
        return self._P_components
    @components.setter
    def components(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property components input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_components=value
    @components.deleter
    def components(self):
        del self._P_components


    @property
    def depends(self):
        return self._P_depends
    @depends.setter
    def depends(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property depends input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property depends_names input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_depends_names=value
    @depends_names.deleter
    def depends_names(self):
        del self._P_depends_names


    @property
    def rackid(self):
        return self._P_rackid
    @rackid.setter
    def rackid(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property rackid input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rackid=value
    @rackid.deleter
    def rackid(self):
        del self._P_rackid


    @property
    def datacenter_name(self):
        return self._P_datacenter_name
    @datacenter_name.setter
    def datacenter_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property datacenter_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_datacenter_name=value
    @datacenter_name.deleter
    def datacenter_name(self):
        del self._P_datacenter_name


    @property
    def pod_name(self):
        return self._P_pod_name
    @pod_name.setter
    def pod_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property pod_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_pod_name=value
    @pod_name.deleter
    def pod_name(self):
        del self._P_pod_name


    @property
    def rack_name(self):
        return self._P_rack_name
    @rack_name.setter
    def rack_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rack_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rack_name=value
    @rack_name.deleter
    def rack_name(self):
        del self._P_rack_name


    @property
    def datacenter_label(self):
        return self._P_datacenter_label
    @datacenter_label.setter
    def datacenter_label(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property datacenter_label input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_datacenter_label=value
    @datacenter_label.deleter
    def datacenter_label(self):
        del self._P_datacenter_label


    @property
    def pod_label(self):
        return self._P_pod_label
    @pod_label.setter
    def pod_label(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property pod_label input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_pod_label=value
    @pod_label.deleter
    def pod_label(self):
        del self._P_pod_label


    @property
    def rack_label(self):
        return self._P_rack_label
    @rack_label.setter
    def rack_label(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property rack_label input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rack_label=value
    @rack_label.deleter
    def rack_label(self):
        del self._P_rack_label


    @property
    def U(self):
        return self._P_U
    @U.setter
    def U(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property U input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_U=value
    @U.deleter
    def U(self):
        del self._P_U


    @property
    def rackpos(self):
        return self._P_rackpos
    @rackpos.setter
    def rackpos(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property rackpos input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_rackpos=value
    @rackpos.deleter
    def rackpos(self):
        del self._P_rackpos


    @property
    def acl(self):
        return self._P_acl
    @acl.setter
    def acl(self, value):
        
        if not isinstance(value, dict) and value is not None:
            if isinstance(value, basestring) and j.basetype.dictionary.checkString(value):
                value = j.basetype.dictionary.fromString(value)
            else:
                msg="property acl input error, needs to be dict, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: asset, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta


    def new_interface(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","interface")()
        else:
            value2=value
        
        self._P_interfaces.append(value2)
        if self._P_interfaces[-1].__dict__.has_key("_P_id"):
            self._P_interfaces[-1].id=len(self._P_interfaces)
        return self._P_interfaces[-1]
        
    

    def new_component(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","component")()
        else:
            value2=value
        
        self._P_components.append(value2)
        if self._P_components[-1].__dict__.has_key("_P_id"):
            self._P_components[-1].id=len(self._P_components)
        return self._P_components[-1]
        
    

    def new_comment(self,value=None):

        if value==None:
            value2=j.core.codegenerator.getClassJSModel("osismodel","oss","comment")()
        else:
            value2=value
        
        self._P_comments.append(value2)
        if self._P_comments[-1].__dict__.has_key("_P_id"):
            self._P_comments[-1].id=len(self._P_comments)
        return self._P_comments[-1]
        
    
