from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database

class ChannelsNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "Name": "Product-Marketing",
    "Describe": "information alignment from squads of Product and Marketing",
    "ChatType": "Channel",
    "ChatId": 1,
}

database.local["Channels"] = [exemple]

def getChannels():
    return jsonify(database.local["Channels"])

def newChannel(request_json):
    res_channel = request_json
    if('Name' in res_channel.keys()):
        for channel in database.local["Channels"]:
            if(channel['Id'] == res_channel['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Channels"].append(res_channel)
        return jsonify(database.local["Channels"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     