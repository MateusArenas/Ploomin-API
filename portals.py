from flask import jsonify, request

class PortalsNaoExisteException(Exception):
    pass

database_portals = [{
    "Id": 1,
    "Name": "A1",
    "OriginTribe": { 
        "Id": 1, 
        "Name": "custom experience",
        "Members": [{"Id": 12, "Name": "Mateus", "SquadId": 2, "SquadName": "Product"}], 
        "Date": "", "ManagersId": [21, 43, 31, 12],
    },
    "Tribes": [{"Id": 1, "Name": 'custom experience'}, {"Id": 3, "Name": 'Ploomes'}],
    "Members": [{"Id": 12, "Name": "Mateus", "SquadId": 2, "SquadName": "Product"}], 
    "Content": { "Channel": "database['Channels'][0]"},
}]

def getPortals():
    return jsonify(database_portals)

def newPortal(request_json):
    res_portal = request_json
    if('Name' in res_portal.keys()):
        for portal in database_portals:
            if(portal['Id'] == res_portal['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database_portals.append(res_portal)
        return jsonify(database_portals)
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     