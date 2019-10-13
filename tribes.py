from flask import jsonify, request

class TribesNaoExisteException(Exception):
    pass

database_tribes = [{
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

def getTribes():
    return jsonify(database_tribes)

def newTribe(request_json):
    res_tribe = request_json
    if('Name' in res_tribe.keys()):
        for tribe in database_tribes:
            if(tribe['Id'] == res_tribe['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database_tribes.append(res_tribe)
        return jsonify(database_tribes)
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     