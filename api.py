from Banco_de_dados import Banco
from flask import Blueprint, request, jsonify, make_response, render_template
from flask_httpauth import HTTPBasicAuth

bd_api = Blueprint('api', __name__, url_prefix='/formulario')
auth = HTTPBasicAuth()
banco = Banco()


@auth.get_password
def virificar_acesso(username):
    """
    verifica o acesso para o REST
    :param username: nome de usuario
    :return: senha: senha do usuario
    """
    if username == 'Wevertom':
        return '123456789'
    else:
        return None


@auth.error_handler
def acesso_negado():
    return make_response(jsonify({'Erro': '<h4>acesso negado !</h4>'}), 403)


@bd_api.route('/registrado', methods=['POST'])
def salvar():
    data = {
        'nome': request.form['nome'],
        'numero_cartao': request.form['numero_cartao'],
        'cvv':  request.form['cvv'],
        'validade': request.form['validade'],
        'cpf': request.form['cpf']
    }
    banco.registrar(data)
    return make_response(render_template('page_cadastrado.html'), 200)


@bd_api.route('/listar', methods=['GET'])
@bd_api.route('/listar/<int:id>', methods=['GET'])
@auth.login_required
def listar(id=None):
    if id != None and id > len(banco.listar()):
        return make_response(jsonify('<h4>O item {} não existe </h4>'.format(id)))
    else:
        lista = banco.listar(id)
        return jsonify({'lista': lista})


@bd_api.route('/deletar/<int:id>', methods=['DELETE'])
@auth.login_required
def apagar(id=None):
    if id != None:
        pessoas = (id['id'] for id in banco.listar())
        if id in pessoas:
            banco.apagar(id)
            return make_response(jsonify('<h4>O item {} foi excluido </h4>'.format(id)))
        else:
            return make_response(jsonify('<h4>O item {} não existe </h4>'.format(id)))
    else:
        return make_response(jsonify({'erro': '<h4>Banco vasio !</h4>'}))