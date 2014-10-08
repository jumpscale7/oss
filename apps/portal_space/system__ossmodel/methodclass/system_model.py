from JumpScale import j
import inspect
import ujson as json

class system_ossmodel(j.code.classGetBase()):
    """
    get an object
    
    """
    def __init__(self):
        
        self._te={}
        self.actorname="ossmodel"
        self.appname="system"
        self.osis = j.core.osis.getClient(user='root')
        self.osisclients={}
        self.specs=None

        # cl.updateSearch("name:kristof","organization:other")

    def _getOsisClient(self,type):
        if not self.osisclients.has_key(type):
            self.osisclients[type] = j.core.osis.getClientForCategory(self.osis, 'oss', type)
        return self.osisclients[type]

    def _getSpecs(self,type):
        import JumpScale.baselib.specparser
        if self.specs==None:
            j.core.specparser.parseSpecs("%s/apps/osis/logic/oss/"%j.dirs.baseDir,"oss","model")
            self.specs= j.core.specparser.specs
        key="model_oss_model_%s"%type
        if not self.specs.has_key(key):
            raise RuntimeError("Could not find specs for %s"%type)
        return self.specs[key]

    def simpleSearch(self, type, query, **kwargs):
        """
        find object
        format query:
            fieldname:val fieldname2:val2 @sort:name,size @size:10 @start:2 @fields:name
        the @... fields are metadata
        the others are combinations to look for
        """
        cl=self._getOsisClient(type)
        # params={}
        # params["query"]=query
        # params["sort"]=sort
        # tags=j.core.tags.getObject(query)
        # params=tags.getDict()

        # query+=" @sort:sort"

        result=cl.search(query=query)
        return result    


    def deleteSearch(self, type, query, **kwargs):
        """
        find object
        format query:
        fieldname:val fieldname2:val2
        param:type type of the object e.g. user or organization
        param:query query to find info
        result str
        """
        cl=self._getOsisClient(type)
        return cl.deleteSearch(query)

    def destroy(self, type, **kwargs):
        """
        destroy fill database with specified type
        param:type type of the object e.g. user or organization
        """
        cl=self._getOsisClient(type)
        result=cl.destroy()

    def demodata(self, type, **kwargs):
        """
        fill database with demo data
        param:type type of the object e.g. user or organization
        """
        cl=self._getOsisClient(type)
        result=cl.demodata()

    def updateSearch(self, type, query, update, **kwargs):
        """
        find object
        format query:
        fieldname:val fieldname2:val2
        param:type type of the object e.g. user or organization
        param:query query to find info
        param:update update key:value pairs
        result str
        """
        return cl.updateSearch(query, update)


    def new(self, type, **kwargs):
        """
        param:type type of the object e.g. user,organization
        result json
        """
        cl=self._getOsisClient(type)
        obj=cl.new()

        methods=[item[0] for item in inspect.getmembers(obj) if item[0].find("new")==0]
        for method in methods:
            meth=eval("obj.%s"%method)
            meth()

        obj.guid=obj.guid.replace("-","")

        return obj.obj2dict()


    def get(self, type, guid="",id=0, **kwargs):
        """
        param:type type of the object e.g. user,organization
        param:id unique id to get to object
        result json
        """

        cl=self._getOsisClient(type)
        obj=None
        if (guid=="" or guid==None) and (id=="" or id==0 or id==None):
            raise RuntimeError("guid or id need to be specified.")
        if guid<>"" and guid<>None:
            obj=cl.get(key=guid)
        elif id<>"" or id<>0:
            obj=cl.get(key=int(id))
            
        if obj==None:            
            raise RuntimeError("Did not find object with guid:%s or id:%s from type:%s"%(guid,id,type))
        return obj.obj2dict()    

    
    def exists(self, type, guid="",id=0, **kwargs):
        """
        check if object exists
        param:type type of the object e.g. user,organization
        param:guid unique id to get to object
        result bool
        """
        cl=self._getOsisClient(type)
        if (guid=="" or guid==None) and (id=="" or id==0 or id==None):
            raise RuntimeError("guid or id need to be specified.")
        obj=None
        if guid<>"" and guid<>None:
            obj=cl.get(guid)
        elif id<>"" or id<>0:
            obj=cl.get(int(id))
        return not obj==None

    def getdoc(self,  **kwargs):
        """
        get schema all known objects in easy readable format
        result json
        """        
        # specs=self._getSpecs(type)
        path="%s/apps/osis/logic/oss/model.spec"%j.dirs.baseDir
        return j.system.fs.fileGetContents(path)

    def getschema(self, type, **kwargs):
        """
        get schema of an object in json
        param:type type of the object e.g. user,organization
        result json
        there is a linenr in the return that refers to line nr in specs which you can retrieve using method getdoc
        """
        specs=self._getSpecs(type)
        return specs
    
    def delete(self, type, guid="",id=0, **kwargs):
        """
        delete an object
        param:type type of the object e.g. user,organization
        param:id unique id to get to object
        result json
        """
        
        cl=self._getOsisClient(type)
        if (guid=="" or guid==None) and (id=="" or id==0 or id==None):
            raise RuntimeError("guid or id need to be specified.")
        if guid<>"" and guid<>None:
            obj=cl.delete(guid)
        elif id<>"" or id<>0:
            obj=cl.delete(int(id))         
        return "OK"          

    def set(self, type, data, **kwargs):
        """
        set an object
        param:type type of the object e.g. user,organization
        param:id unique id to get to object
        param:data is json structured data of object
        result json
        """
        val=json.loads(data)
        cl=self._getOsisClient(type)
        
        temp,temp,guid=cl.set(val)

        obj=cl.get(guid)
        if obj==None:            
            raise RuntimeError("Did not find object just saved with guid:%s"%guid)
        return obj.obj2dict()    
