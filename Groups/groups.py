from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database
import utils as utils

class GroupsNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "Name": "Devs",
    "Describe": "Group turned for developers",
    "ChatType": "Group",
    "ChatId": 1,
    "Date": "Wed, 23 Oct 2019 00:12:37 GMT"
}

database.local["Groups"] = [exemple]

def getGroups():
    return jsonify(database.local["Groups"])

def newGroup(request_json):
    res_group = request_json
    res_group["Date"] = utils.createdDate()
    if('Name' in res_group.keys()):
        for group in database.local["Groups"]:
            if(group['Id'] == res_group['Id']):
                res_group["Id"] = utils.createdId(database.local["Groups"])
        database.local["Groups"].append(res_group)
        return jsonify(database.local["Groups"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     