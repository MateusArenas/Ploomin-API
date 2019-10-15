from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database

class GroupsNaoExisteException(Exception):
    pass

database.local["Groups"] = [{
    "Id": 1 , "Name": "custom experience", "Members": [{"Id": 12, "Name": "Mateus", "SquadId": 2, "SquadName": "Product"}], 
    "Date": "", "ManagersId": [21, 43, 31, 12],
    "Messages": [{
        "Id": 2, "Date": "", 
        "Watchers": [{"Id":21 , "Name": "Vitor", "ReceivedDate": "", "WatchDate": ""}],
        "Content": {"PhotoUrl": "https...", "Audio": "....", "Archive": "...", "Video": "...", "Text": "sim, é muito legal!"},
        "Reply": {"Id": 1, "Content": "vcs sabem oque é?"}
    }],
    "Channels": [{"Id": 1, "Title": "unit tests", "Describer": "melhor forma para prevenção de bugs." }]
}]

def getGroups():
    return jsonify(database.local["Groups"])

def newGroup(request_json):
    res_group = request_json
    if('Name' in res_group.keys()):
        for group in database.local["Groups"]:
            if(group['Id'] == res_group['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Groups"].append(res_group)
        return jsonify(database.local["Groups"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     