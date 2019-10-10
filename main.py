from flask import Flask, jsonify, request

app = Flask(__name__)                              

database = {}
database['USER'] = []
                                                 

@app.route('/hello')                         
def ola():
    return 'Olá mundo!'  

Groups: [{
    Id: 1 , Name: 'custom experience', Members: [{Id: 12, Name: 'Mateus', SquadId: 2, SquadName: 'Product'}}], 
    Date: '', ManagersId: [21, 43, 31, 12],
    Messages: [{
        Id: 2, Date: '', 
        Watchers: [{Id:21, Name: 'Vitor', ReceivedDate: '', WatchDate: ''}],
        Content: {PhotoUrl: 'https...', Audio: '....', Archive: '...', Video: '...', Text: 'sim, é muito legal!'},
        Reply: {Id: 1, Content: 'vcs sabem oque é?'}
    }],
    Channels: [{Id: 1, Title: 'unit tests', Describer: 'melhor forma para prevenção de bugs.' }]
}]
'''os canais serão separados sem dependecia dos grupos, pois um grupo pode ser finalizado e um canal não deve ir embora com ele'''
Channels: [{
    Id: 1, Title: 'unit tests', Describer: 'melhor forma para prevenção de bugs.',
    Created: { Group: {Id: 1, Name: 'custom experience'}, Founder: {Id: 12, Name: 'Mateus'}},
    Groups: [{Id: 1, Name: 'custom experience'}, {Id: 3, Name: 'Ploomes'}], #uma coisa incrivel, dentro dos grupos serão criado canais. que serão uma porta para a comunicação com membros de outros grupos
    Members: [{Id: 12, Name: 'Mateus', SquadId: 2, SquadName: 'Product'}}], 
    Date: '', ManagersId: [21, 43, 31, 12],
    Messages: [{
        Id: 2, Date: '', 
        Watchers: [{Id:21, Name: 'Vitor', ReceivedDate: '', WatchDate: ''}],
        Content: {PhotoUrl: 'https...', Audio: '....', Archive: '...', Video: '...', Text: 'sim, é muito legal!'},
        Reply: {Id: 1, Content: 'vcs sabem oque é?'}
    }],
}]


@app.route('/groups', methods=['POST'])            
def new_group():
    new_group = request.json
    if('name' in novo_aluno.keys()):
        for aluno in database['ALUNO']:
            if(aluno['id'] == novo_aluno['id']):
                return jsonify({'erro':'id ja utilizada'}), 400
        database['ALUNO'].append(novo_aluno)
        return jsonify(database['ALUNO'])
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
							         
