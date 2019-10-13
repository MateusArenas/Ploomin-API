from flask import jsonify, request

class ChannelsNaoExisteException(Exception):
    pass

database_channels = [{
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
    return jsonify(database_channels)

def newChannel(request_json):
    res_channel = request_json
    if('Name' in res_channel.keys()):
        for channel in database_channels:
            if(channel['Id'] == res_channel['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database_channels.append(res_channel)
        return jsonify(database_channels)
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     