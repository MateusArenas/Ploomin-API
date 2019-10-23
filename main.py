import Users.users as users
from Users.users import UsersNaoExisteException

import Squads.squads as squads
from Squads.squads import SquadsNaoExisteException

import Groups.groups as groups
from Groups.groups import GroupsNaoExisteException

import Channels.channels as channels
from Channels.channels import ChannelsNaoExisteException

import Portals.portals as portals
from Portals.portals import PortalsNaoExisteException

import Chats.chats as chats
from Chats.chats import ChatsNaoExisteException

import Messages.messages as messages
from Messages.messages import MessagesNaoExisteException

import Members.members as members
from Members.members import MembersNaoExisteException

from flask import Flask, jsonify, request

class MainNaoExisteException(Exception):
    pass

app = Flask(__name__)                             

'''os canais serão separados sem dependecia dos grupos, pois um grupo pode ser finalizado e um canal não deve ir embora com ele'''


'''Existirá Portals que serão linkagens  '''


''' ---- U S E R S ----'''
@app.route('/Users')                    
def getUsers():
    return users.getUsers()

@app.route('/Users', methods=['POST'])            
def newUser():
    return users.newUser(request.json)     

@app.route('/Users/<int:user_id>', methods=['GET'])                                                                                                                                                                                       
def search_user(user_id):                                               
    return users.search_user(user_id)                                                

@app.route('/Users/<int:user_id>', methods=['PUT'])                                                                                                                                                                                       
def edited_user(user_id):
    return users.edited_user(request.json, user_id)
                                                                                   
@app.route('/Users/<int:user_id>', methods=['DELETE'])                                                                                                                                                                                       
def deleted_user(user_id):
    return users.deleted_user(user_id)

''' ---- T R I B E S ----'''
@app.route('/Squads')                    
def getSquads():
    return squads.getSquads()

@app.route('/Squads', methods=['POST'])            
def newSquad():
    return squads.newSquad(request.json)    

''' ---- G R O U P S ----'''
@app.route('/Groups')                    
def getGroups():
    return groups.getGroups()

@app.route('/Groups', methods=['POST'])            
def newGroup():
    return groups.newGroup(request.json)    

''' ---- C H A N N E L S ----'''
@app.route('/Channels')                    
def getChannels():
    return channels.getChannels()

@app.route('/Channels', methods=['POST'])            
def newChannel():
    return channels.newChannel(request.json)   

''' ---- P O R T A L S ----'''
@app.route('/Portals')                    
def getPortals():
    return portals.getPortals()

@app.route('/Portals', methods=['POST'])            
def newPortal():
    return portals.newPortal(request.json)  

''' ---- C H A T S ----'''
@app.route('/Chats')                    
def getChats():
    return chats.getChats()

@app.route('/Chats', methods=['POST'])            
def newChat():
    return chats.newChat(request.json) 

''' ---- M E S S A G E S ----'''
@app.route('/Messages')                    
def getMessages():
    return messages.getMessages()

@app.route('/Messages', methods=['POST'])            
def newMessage():
    return messages.newMessage(request.json)  

''' ---- M E M B E R S ----'''
@app.route('/Members')                    
def getMembers():
    return members.getMembers()

@app.route('/Members', methods=['POST'])            
def newMember():
    return members.newMember(request.json)  

''' ---- ------------------------ ----'''       

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
							         
