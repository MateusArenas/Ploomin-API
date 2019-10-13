import users 
from users import UsersNaoExisteException

import tribes
from tribes import TribesNaoExisteException

import channels
from channels import ChannelsNaoExisteException

import portals
from portals import PortalsNaoExisteException

from flask import Flask, jsonify, request

class MainNaoExisteException(Exception):
    pass

app = Flask(__name__)                              

database = {}
                                                 

@app.route('/hello')                         
def ola():
    return 'Olá mundo!'  

database['Users'] = users.database_users

database['Tribes'] = tribes.database_tribes

'''os canais serão separados sem dependecia dos grupos, pois um grupo pode ser finalizado e um canal não deve ir embora com ele'''
database['Channels'] = channels.database_channels

print(database['Channels'])

'''Existirá Portals que serão linkagens  '''

database['Portals'] = portals.database_portals

''' ---- U S E R S ----'''
@app.route('/users')                    
def getUsers():
    return users.getUsers()

@app.route('/users', methods=['POST'])            
def newUser():
    return users.newUser(request.json)     

''' ---- T R I B E S ----'''
@app.route('/tribes')                    
def getTribes():
    return tribes.getTribes()

@app.route('/tribes', methods=['POST'])            
def newTribe():
    return tribes.newTribe(request.json)    

''' ---- C H A N N E L S ----'''
@app.route('/channels')                    
def getChannels():
    return channels.getChannels()

@app.route('/channels', methods=['POST'])            
def newChannel():
    return channels.newChannel(request.json)   

''' ---- P O R T A L S ----'''
@app.route('/portals')                    
def getPortals():
    return portals.getPortals()

@app.route('/portals', methods=['POST'])            
def newPortal():
    return portals.newPortal(request.json)  

''' ---- ------------------------ ----'''

@app.route('/groups')                    
def alunos():
    return jsonify(database['Groups'])

@app.route('/groups', methods=['POST'])            
def new_group():
    res_group = request.json
    if('Name' in res_group.keys()):
        for gorup in database['Groups']:
            if(gorup['Id'] == res_group['Id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database['Groups'].append(res_group)
        return jsonify(database['Groups'])
    else:
        return jsonify({'erro':'aluno sem nome'}), 400                  

'''@app.route('/')
def all():
    return jsonify(database)             
                                                                                                         
@app.route('/zoada')
def all_zoada():
    return database                        
                                                      
@app.route('/reseta', methods=['POST'])
def all_delete():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return 'alunos e professores resetados com sucesso!'      

@app.route('/alunos')                    
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/alunos', methods=['POST'])            
def novo_aluno():
    novo_aluno = request.json
    if('nome' in novo_aluno.keys()):
        for aluno in database['ALUNO']:
            if(aluno['id'] == novo_aluno['id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database['ALUNO'].append(novo_aluno)
        return jsonify(database['ALUNO'])
    else:
        return jsonify({'erro':'aluno sem nome'}), 400


@app.route('/alunos/<int:id_aluno>', methods=['GET'])                                                                                                                                                                                       
def localiza_aluno(id_aluno):                                               
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'aluno nao encontrado'
    return resp                                                

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])                                                                                                                                                                                       
def edita_aluno(id_aluno):
    data_aluno = request.json
    print(data_aluno)
    if('nome' in data_aluno.keys()):
        for aluno in database['ALUNO']:
            if aluno['id'] == id_aluno:
                aluno['nome'] = data_aluno['nome']
                return jsonify(aluno)
        return jsonify({'erro':'aluno nao encontrado'}), 400        
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'aluno sem nome'}), 400

                                                                                      
@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])                                                                                                                                                                                       
def deleta_aluno(id_aluno):
    if(type(id_aluno) == int):
        for aluno in database['ALUNO']:
            if aluno['id'] == id_aluno:
                database['ALUNO'].remove(aluno)
                return 'deletado com sucesso'
    message = {
        'erro': 'aluno nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'aluno nao encontrado'
    return resp
                                                                                           


@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/professores', methods=['POST'])            
def novo_professor():
    novo_professor = request.json
    if('nome' in novo_professor.keys()):
        for professor in database['PROFESSOR']:
            if(professor['id'] == novo_professor['id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database['PROFESSOR'].append(novo_professor)
        return jsonify(database['PROFESSOR'])
    else:
        return jsonify({'erro':'professor sem nome'}), 400


@app.route('/professores/<int:id_professor>', methods=['GET'])                                                                                                                                                                                       
def localiza_professor(id_professor):                                               
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return jsonify(professor)
    message = {
        'erro': 'professor nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'professor nao encontrado'
    return resp                                                

@app.route('/professores/<int:id_professor>', methods=['PUT'])                                                                                                                                                                                       
def edita_professor(id_professor):
    data_professor = request.json
    if('nome' in data_professor.keys()):
        for professor in database['PROFESSOR']:
            if professor['id'] == id_professor:
                professor['nome'] = data_professor['nome']
                return jsonify(professor)
        return jsonify({'erro':'professor nao encontrado'}), 400        
    message = {
        'erro': 'professor nao encontrado',
        'status_code': 400,
    }
    return jsonify({'erro':'professor sem nome'}), 400

                                                                                      
@app.route('/professores/<int:id_professor>', methods=['DELETE'])                                                                                                                                                                                       
def deleta_professor(id_professor):
    if(type(id_professor) == int):
        for professor in database['PROFESSOR']:
            if professor['id'] == id_professor:
                database['PROFESSOR'].remove(professor)
                return 'deletado com sucesso'
    message = {
        'erro': 'professor nao encontrado',
        'status_code': 400,
    }
    resp = jsonify(message)
    resp.status_code = 400
    resp.erro = 'professor nao encontrado'
    return resp
'''                                                                                       


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)   
							         
