from flask import jsonify, request

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database

class ChannelsNaoExisteException(Exception):
    pass

database.local["Channels"] = [{
    "Id": 1, "Title": 'unit tests', 
    "Describer": 'melhor forma para prevenção de bugs.',
    "Portals": [ { "Id": 1, "Name": "A1" } ],
    "Created": { "Tribe": {"Id": 1, "Name": 'custom experience'}, "Founder": {"Id": 12, "Name": 'Mateus'}},
    "Tribes": [{"Id": 1, "Name": 'custom experience'}, {"Id": 3, "Name": 'Ploomes'}], #uma coisa incrivel, dentro dos grupos serão criado canais. que serão uma porta para a comunicação com membros de outros grupos
    "Members": [{"Id": 12, "Name": 'Mateus', "SquadId": 2, "SquadName": 'Product'}], 
    "Date": '', "ManagersId": [21, 43, 31, 12],
    "Messages": [{
        "Id": 2, "Date": '', 
        "Watchers": [{"Id": 21, "Name": 'Vitor', "ReceivedDate": '', "WatchDate": ''}],
        "Content": {"PhotoUrl": 'https...', "Audio": '....', "Archive": '...', "Video": '...', "Text": 'sim, é muito legal!'},
        "Reply": {"Id": 1, "Content": 'vcs sabem oque é?'}
    }],
}]
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