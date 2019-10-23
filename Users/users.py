from flask import jsonify, request
import os as os

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database



class UsersNaoExisteException(Exception):
    pass

exemple = {
    "Id": 1,
    "Name": "Mateus",
    "Email": "MateusArenas97@gmail.com",
    "UserName" : "MateusArenas",
    "Password": "kabhdiu3e3a",
    "SquadId": 1,
}

database.local["Users"] = [exemple]

def getUsers():
    return jsonify(database.local["Users"])

def newUser(request_json):
    res_user = request_json
    if('Name' in res_user.keys()):
        for user in database.local["Users"]:
            if(user['Id'] == res_user['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database.local["Users"].append(res_user)
        return jsonify(database.local["Users"])
    else:
        return jsonify({'erro':'usuario sem nome'}), 400  

def search_user(user_id):
    for user in database.local["Users"]:
            if user['id'] == user_id:
                return jsonify(user)
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'aluno nao encontrado'
    return resp   

def edited_user(request_json,user_id):
    data_user = request_json
    if('nome' in data_user.keys()):
        for user in database.local["Users"]:
            if user['id'] == user_id:
                user['nome'] = data_user['nome']
                return jsonify(user)
        return jsonify({'erro':'aluno nao encontrado'}), 400        
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'aluno sem nome'}), 400

def deleted_user(user_id):
    if(type(user_id) == int):
        for user in database.local["Users"]:
            if user['id'] == user_id:
                database.local["Users"].remove(user)
                return 'deletado com sucesso'
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'aluno nao encontrado'
    return resp