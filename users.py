from flask import jsonify, request

class UsersNaoExisteException(Exception):
    pass

database_users = [{
    "Id": 1,
    "Name": "Mateus",
    "Squad": {"Id": 2, "Name": "Product"},
    "Email": "MateusArenas97@gmail.com",
    "Password": "kabhdiu3e3a",
    "Host": {"Id": 5, "Name": 'Matheus Pagani', "Email": "MateusPagani@gmail.com"},
}]

def getUsers():
    return jsonify(database_users)

def newUser(request_json):
    res_user = request_json
    if('Name' in res_user.keys()):
        for user in database_users:
            if(user['Id'] == res_user['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database_users.append(res_user)
        return jsonify(database_users)
    else:
        return jsonify({'erro':'usuario sem nome'}), 400     