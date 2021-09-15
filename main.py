from flask import Flask, render_template, make_response

from api import bd_api

app = Flask('sorteio')
app.register_blueprint(bd_api)


@app.route('/')
def home():
    """
    Pagina principal
    :return: rederiza a pagina home.html
    """
    return make_response(render_template('home.html'), 200)


@app.errorhandler(404)
def not_found(error):
    """
    Pagina de erro (pagina inexistente)
    :param error: Tipo de erro
    :return: rederiza a pagina page_error.html
    """
    return make_response(render_template('page_error.html'), 404)


if __name__ == '__main__':
    app.run(use_reloader=True)