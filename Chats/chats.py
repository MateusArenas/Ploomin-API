from flask import jsonify, request
import os as os

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database



class ChatsNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "TypeId": 1,
    "Type": "Channel",
}

database.local["Chats"] = [exemple]

def getChats():
    return jsonify(database.local["Chats"])

def newChat(request_json):
    res_chat = request_json
    if('ChatId' in res_chat.keys()):
        for chat in database.local["Chats"]:
            if(chat['Id'] == res_chat['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Chats"].append(res_chat)
        return jsonify(database.local["Chats"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400  

def search_chat(chat_id):
    for chat in database.local["Chats"]:
            if chat['id'] == chat_id:
                return jsonify(chat)
    message = {
        'erro': 'chat nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'chat nao encontrado'
    return resp   

def edited_chat(request_json,chat_id):
    data_chat = request_json
    if('nome' in data_chat.keys()):
        for chat in database.local["Chats"]:
            if chat['id'] == chat_id:
                chat['nome'] = data_chat['nome']
                return jsonify(chat)
        return jsonify({'erro':'chat nao encontrado'}), 400        
    message = {
        'erro': 'chat nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'chat sem nome'}), 400

def deleted_chat(chat_id):
    if(type(chat_id) == int):
        for chat in database.local["Chats"]:
            if chat['id'] == chat_id:
                database.local["Chats"].remove(chat)
                return 'deletado com sucesso'
    message = {
        'erro': 'chat nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'chat nao encontrado'
    return resp