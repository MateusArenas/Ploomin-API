from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database
import utils as utils

class SquadsNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "Name": "Product",
    "Describe": "this squad has responsibility for the product",
    "ChatType": "Squad",
    "ChatId": 1,
    "Date": "Wed, 23 Oct 2019 00:12:37 GMT"
}

database.local["Squads"] = [exemple]

def getSquads():
    return jsonify(database.local["Squads"])

def newSquad(request):
    if 'UserKey' in request.headers:
        user_key = request.headers.get('UserKey')
        if utils.validateToken(user_key):
                res_squad = request.json
                res_squad["Date"] = utils.createdDate()
                if('Name' in res_squad.keys()):
                    for squad in database.local["Squads"]:
                        if(squad['Id'] == res_squad['Id']):
                            res_squad["Id"] = utils.createdId(database.local["Squads"])
                    database.local["Squads"].append(res_squad)
                    return jsonify(res_squad)
                else:
                    return jsonify({'erro':'usuario sem nome'}), 400     
        return jsonify({'erro':'usuario com o token ivalido'}), 400 
    return jsonify({'erro':'usuario sem token'}), 400  