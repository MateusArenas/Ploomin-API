from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database

class PortalsNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "Name": "177C",
    "ChatId": 1,
}

database.local["Portals"] = [exemple]

def getPortals():
    return jsonify(database.local["Portals"])

def newPortal(request_json):
    res_portal = request_json
    if('Name' in res_portal.keys()):
        for portal in database.local["Portals"]:
            if(portal['Id'] == res_portal['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Portals"].append(res_portal)
        return jsonify(database.local["Portals"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     