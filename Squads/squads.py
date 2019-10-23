from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database

class SquadsNaoExisteException(Exception):
    pass

exemple = {
    "Name": "Product",
    "Describe": "this squad has responsibility for the product",
    "ChatType": "Squad",
    "ChatId": 1,
}

database.local["Squads"] = [exemple]

def getSquads():
    return jsonify(database.local["Squads"])

def newSquad(request_json):
    res_squad = request_json
    if('Name' in res_squad.keys()):
        for squad in database.local["Squads"]:
            if(squad['Id'] == res_squad['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Squads"].append(res_squad)
        return jsonify(database.local["Squads"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     