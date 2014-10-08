from JumpScale import j

class oss_comment_osismodelbase(j.code.classGetJSRootModelBase()):
    def __init__(self):
        self._P_comment=""
    
        self._P_time=0
    
        self._P_author=0
    
        self._P_author_name=""
    
        self._P_id=0
    
        self._P_guid=""
    
        self._P__meta=list()
    
        self._P__meta=["osismodel","oss","comment",1] #@todo version not implemented now, just already foreseen
    

        pass

    @property
    def comment(self):
        return self._P_comment
    @comment.setter
    def comment(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property comment input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_comment=value
    @comment.deleter
    def comment(self):
        del self._P_comment


    @property
    def time(self):
        return self._P_time
    @time.setter
    def time(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property time input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_time=value
    @time.deleter
    def time(self):
        del self._P_time


    @property
    def author(self):
        return self._P_author
    @author.setter
    def author(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property author input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_author=value
    @author.deleter
    def author(self):
        del self._P_author


    @property
    def author_name(self):
        return self._P_author_name
    @author_name.setter
    def author_name(self, value):
        
        if not isinstance(value, str) and value is not None:
            if isinstance(value, basestring) and j.basetype.string.checkString(value):
                value = j.basetype.string.fromString(value)
            else:
                msg="property author_name input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P_author_name=value
    @author_name.deleter
    def author_name(self):
        del self._P_author_name


    @property
    def id(self):
        return self._P_id
    @id.setter
    def id(self, value):
        
        if not isinstance(value, int) and value is not None:
            if isinstance(value, basestring) and j.basetype.integer.checkString(value):
                value = j.basetype.integer.fromString(value)
            else:
                msg="property id input error, needs to be int, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
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
                msg="property guid input error, needs to be str, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
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
                msg="property _meta input error, needs to be list, specfile: /opt/jumpscale/apps/osis/logic/oss/model.spec, name model: comment, value was:" + str(value)
                raise RuntimeError(msg)
    

        self._P__meta=value
    @_meta.deleter
    def _meta(self):
        del self._P__meta

