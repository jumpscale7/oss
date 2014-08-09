
def main(j, args, params, tags, tasklet):
    params.merge(args)

    doc = params.doc
    tags = params.tags

    params.result = ""


    # spaces = sorted(j.core.portal.active.getSpaces())
    # spacestxt=""
    # for item in spaces:
    #     if item[0] != "_" and item.strip() != "" and item.find("space_system")==-1 and item.find("test")==-1 and  item.find("gridlogs")==-1:
    #         spacestxt += "%s:/%s\n" % (item, item.lower().strip("/"))


    C = """
{{menudropdown: name:Portal
Edit:/system/edit?space=$$space&page=$$page&$$querystr
New:/system/create?space=$$space
--------------
Logout:/system/login?user_logoff_=1
Access:/system/OverviewAccess?space=$$space
System:/system
--------------
OSS:/oss
JPackages:/jpackages
Tests:/tests
--------------
Asset Types:/oss/AssetTypes
Assets:/oss/Assets
Datacenters:/oss/Datacenters
Groups:/oss/Groups
Interfaces:/oss/Interfaces
Interface Types:/oss/InterfaceTypes
Machines:/oss/Machines
Messages:/oss/Messages
Net Addresses:/oss/NetAddrs
Organizations:/oss/Organizations
Projects:/oss/Projects
Racks:/oss/Racks
Sprints:/oss/Sprints
Tickets:/oss/Tickets
Users:/oss/Users
"""
    # C+=spacestxt
    C+='}}'

    if j.core.portal.active.isAdminFromCTX(params.requestContext):
        params.result = C

    params.result = (params.result, doc)

    return params


def match(j, args, params, tags, tasklet):
    return True
