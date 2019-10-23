from flask import jsonify, request
import os as os

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database
import utils as utils

class MembersNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "ChatId": 1,
    "memberId": 1,
    "Date": "Wed, 23 Oct 2019 00:12:37 GMT"
}

database.local["Members"] = [exemple]

def getMembers():
    return jsonify(database.local["Members"])

def newMember(request_json):
    res_member = request_json
    res_member["Date"] = utils.createdDate()
    if('ChatId' in res_member.keys()):
        for member in database.local["Members"]:
            if(member['Id'] == res_member['Id']):
                res_member["Id"] = utils.createdId(database.local["Members"])
        database.local["Members"].append(res_member)
        return jsonify(database.local["Members"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400  

def search_member(member_id):
    for member in database.local["Members"]:
            if member['id'] == member_id:
                return jsonify(member)
    message = {
        'erro': 'member nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'member nao encontrado'
    return resp   

def edited_member(request_json,member_id):
    data_member = request_json
    if('nome' in data_member.keys()):
        for member in database.local["Members"]:
            if member['id'] == member_id:
                member['nome'] = data_member['nome']
                return jsonify(member)
        return jsonify({'erro':'member nao encontrado'}), 400        
    message = {
        'erro': 'member nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'member sem nome'}), 400

def deleted_member(member_id):
    if(type(member_id) == int):
        for member in database.local["Members"]:
            if member['id'] == member_id:
                database.local["Members"].remove(member)
                return 'deletado com sucesso'
    message = {
        'erro': 'member nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'member nao encontrado'
    return resp