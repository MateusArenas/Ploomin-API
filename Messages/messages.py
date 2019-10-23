from flask import jsonify, request
import os as os

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database



class MessagesNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "ChatId": 1,
    "Content": "Hey guys, I created this channel to align ourselves, about last month.",
    "UserName": "MateusArenas",
    "Email": "MateusArenas97@gmail.com",
    "Date": "Tue Oct 22 2019 23:09:19 GMT-0300 (Brasilia Standard Time)",
}

database.local["Messages"] = [exemple]

def getMessages():
    return jsonify(database.local["Messages"])

def newMessage(request_json):
    res_message = request_json
    if('ChatId' in res_message.keys()):
        for message in database.local["Messages"]:
            if(message['Id'] == res_message['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Messages"].append(res_message)
        return jsonify(database.local["Messages"])
    else:
        return jsonify({'erro':'Message sem nome'}), 400  

def search_message(message_id):
    for message in database.local["Messages"]:
            if message['id'] == message_id:
                return jsonify(message)
    message = {
        'erro': 'message nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'message nao encontrado'
    return resp   

def edited_message(request_json,message_id):
    data_message = request_json
    if('nome' in data_message.keys()):
        for message in database.local["Messages"]:
            if message['id'] == message_id:
                message['nome'] = data_message['nome']
                return jsonify(message)
        return jsonify({'erro':'message nao encontrado'}), 400        
    message = {
        'erro': 'message nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'message sem nome'}), 400

def deleted_message(message_id):
    if(type(message_id) == int):
        for message in database.local["Messages"]:
            if message['id'] == message_id:
                database.local["Messages"].remove(message)
                return 'deletado com sucesso'
    message = {
        'erro': 'message nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'message nao encontrado'
    return resp