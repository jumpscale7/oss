[actor] 
    """
    
    """    

    method:new
        """     
        create a new object and return empty json
        """
        var:type str,,type of the object e.g. user,organization
        result:json

    method:get
        """     
        get an object
        """
        var:type str,,type of the object e.g. user,organization
        var:id int,,id or gui only use 1 @tags: optional 
        var:guid str,,unique id to get to object @tags: optional 
        result:json

    method:delete
        """     
        delete an object
        """
        var:type str,,type of the object e.g. user,organization
        var:id int,,id or gui only use 1 @tags: optional 
        var:guid str,,unique id to get to object @tags: optional 
        result:json

    method:exists
        """     
        check if object exists
        """
        var:type str,,type of the object e.g. user,organization
        var:id int,,id or gui only use 1 @tags: optional 
        var:guid str,,unique id to get to object @tags: optional 
        result:bool


    method:set
        """     
        set an object
        (if guid & id not filled in then will be done automatically)
        if ID filled in, object will be fetched & updated
        same for GUID
        """
        var:type str,,type of the object e.g. user or organization
        var:data str,,is json structured data of object
        result:json

    method:simpleSearch
        """     
        find object
        format query:
            fieldname:val fieldname2:val2 @sort:name,size @size:10 @start:2 @fields:name
        the @... fields are metadata
        the others are combinations to look for
        """
        var:type str,,type of the object e.g. user or organization
        var:query str,,query to find info
        result:list

    method:deleteSearch
        """     
        find object
        format query:
            fieldname:val fieldname2:val2 
        """
        var:type str,,type of the object e.g. user or organization
        var:query str,,query to find info
        result:str

    method:updateSearch
        """     
        find object
        format query:
            fieldname:val fieldname2:val2 
        """
        var:type str,,type of the object e.g. user or organization
        var:query str,,query to find info
        var:update dict,,update key:value pairs
        result:str

    method:getdoc
        """     
        get schema all known objects in easy readable format
        result json
        """
        result:json

    method:getschema
        """     
        get schema of an object in json
        param:type type of the object e.g. user,organization
        result json
        there is a linenr in the return that refers to line nr in specs which you can retrieve using method getdoc
        """
        var:type str,,type of the object e.g. user,organization
        result:json

    method:destroy
        """     
        destroy fill database with specified type
        """
        var:type str,,type of the object e.g. user or organization

    method:demodata
        """     
        fill database with demo data
        """
        var:type str,,type of the object e.g. user or organization @optional