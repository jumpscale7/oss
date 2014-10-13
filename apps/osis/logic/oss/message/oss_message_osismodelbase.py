from JumpScale import j

class oss_message_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_subject=""
    
        self._P_message=""
    
        self._P_destination=list()
    
        self._P_time=0
    
        self._P_type=""
    
        self._P_format=""
    
        self._P_ticket=0
    
        self._P_comments=list()
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","message",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def subject(self):
        return self._P_subject
    @subject.setter
    def subject(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property subject input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_subject=value
    @subject.deleter
    def subject(self):
        del self._P_subject


    @property
    def message(self):
        return self._P_message
    @message.setter
    def message(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property message input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_message=value
    @message.deleter
    def message(self):
        del self._P_message


    @property
    def destination(self):
        return self._P_destination
    @destination.setter
    def destination(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property destination input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_destination=value
    @destination.deleter
    def destination(self):
        del self._P_destination


    @property
    def time(self):
        return self._P_time
    @time.setter
    def time(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time=value
    @time.deleter
    def time(self):
        del self._P_time


    @property
    def type(self):
        return self._P_type
    @type.setter
    def type(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property type input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_type=value
    @type.deleter
    def type(self):
        del self._P_type


    @property
    def format(self):
        return self._P_format
    @format.setter
    def format(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property format input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_format=value
    @format.deleter
    def format(self):
        del self._P_format


    @property
    def ticket(self):
        return self._P_ticket
    @ticket.setter
    def ticket(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property ticket input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_ticket=value
    @ticket.deleter
    def ticket(self):
        del self._P_ticket


    @property
    def comments(self):
        return self._P_comments
    @comments.setter
    def comments(self, value):
        
        if not isinstance(value, list) and value is not None:
            if isinstance(value, basestring) and j.basetype.list.checkString(value):
                value = j.basetype.list.fromString(value)
            else:
                msg="property comments input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
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
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: message, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

