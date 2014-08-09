from JumpScale import j

class system_ossmodel(j.code.classGetBase()):
    """
    create a new object and return empty json
    
    """
    def __init__(self):
        
        self._te={}
        self.actorname="ossmodel"
        self.appname="system"
        #system_ossmodel_osis.__init__(self)
    

        pass

    def delete(self, type, id, guid, **kwargs):
        """
        delete an object
        param:type type of the object e.g. user,organization
        param:id id or gui only use 1
        param:guid unique id to get to object
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method delete")
    

    def deleteSearch(self, type, query, **kwargs):
        """
        find object
        format query:
        fieldname:val fieldname2:val2
        param:type type of the object e.g. user or organization
        param:query query to find info
        result str
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method deleteSearch")
    

    def demodata(self, type, **kwargs):
        """
        fill database with demo data
        param:type type of the object e.g. user or organization
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method demodata")
    

    def destroy(self, type, **kwargs):
        """
        destroy fill database with specified type
        param:type type of the object e.g. user or organization
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method destroy")
    

    def exists(self, type, id, guid, **kwargs):
        """
        check if object exists
        param:type type of the object e.g. user,organization
        param:id id or gui only use 1
        param:guid unique id to get to object
        result bool
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method exists")
    

    def get(self, type, id, guid, **kwargs):
        """
        get an object
        param:type type of the object e.g. user,organization
        param:id id or gui only use 1
        param:guid unique id to get to object
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method get")
    

    def getdoc(self, **kwargs):
        """
        get schema all known objects in easy readable format
        result json
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method getdoc")
    

    def getschema(self, type, **kwargs):
        """
        get schema of an object in json
        param:type type of the object e.g. user,organization
        result json
        there is a linenr in the return that refers to line nr in specs which you can retrieve using method getdoc
        param:type type of the object e.g. user,organization
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method getschema")
    

    def new(self, type, **kwargs):
        """
        param:type type of the object e.g. user,organization
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method new")
    

    def set(self, type, data, **kwargs):
        """
        set an object
        (if guid & id not filled in then will be done automatically)
        if ID filled in, object will be fetched & updated
        same for GUID
        param:type type of the object e.g. user or organization
        param:data is json structured data of object
        result json
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method set")
    

    def simpleSearch(self, type, query, **kwargs):
        """
        find object
        format query:
        fieldname:val fieldname2:val2 @sort:name,size @size:10 @start:2 @fields:name
        the @... fields are metadata
        the others are combinations to look for
        param:type type of the object e.g. user or organization
        param:query query to find info
        result list
        """
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method simpleSearch")
    

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
        #put your code here to implement this method
        raise NotImplementedError ("not implemented method updateSearch")
    
