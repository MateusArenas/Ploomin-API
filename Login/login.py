from flask import jsonify, request
import os as os

# Solution B - If the script importing the module is not in a package
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import database as database
import utils as utils

class LoginNaoExisteException(Exception):
    pass

"""
var headers = new Headers();
var logindata = { 
    "Email": "MateusArenas97@gmail.com",
    "Password": "kabhdiu3e3a"
};
var strify = JSON.stringify(logindata);
fetch('http://localhost:5002/Login', 
{ 	method: 'POST', 
	headers: new Headers({'content-type': 'application/json'}),
	body: strify,
})
.then(response => response.json())
.then((data) => {
	console.log(data.value);
});

qual é a vantagem de ter mais de um servidor, qual é a diferencia, oque da para fazer de diferente de ter somente 1
"""

database.local["Tokens"] = []

def login(request_json):
    res_user = request_json
    result = [user for user in database.local["Users"] if user["Email"] == res_user["Email"]]
    token = utils.createToken()
    if('Email' in res_user.keys() and 'Password' in res_user.keys()):
        if len(result) == 1 and res_user['Password'] == result[0]["Password"]:
            database.local['Tokens'].append({ "UserKey": token, "UserId": result[0]['Id']})
            result[0]['UserKey'] = token
            return jsonify({ "value": result })
    return jsonify({'erro':'usuario sem nome'}), 400  

def logout(user_id):
    if 'Tokens' in database.local.keys():
        for token in database.local["Tokens"]:
            if token['UserId'] == user_id:
                user_key = token['UserKey']
                if utils.validateToken(user_key):
                    database.local['Tokens'].remove(token)
                    return jsonify({'ok':'usuario deslogado'}), 200
    

