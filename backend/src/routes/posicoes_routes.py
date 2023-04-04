from src.controllers import posicoes_controllers
from flask import render_template

def init_app(app):

    @app.route("/")
    def template():
        return render_template('index.html')

    @app.route("/positions", methods=['GET'])
    def read_positions():
        return posicoes_controllers.read()
    
    @app.route("/positions", methods=['POST'])
    def create_positions():
        return posicoes_controllers.create()
    
    @app.route("/positions/<int:id>", methods=['PUT'])
    def update_positions(id):
        return posicoes_controllers.update(id)

    @app.route("/positions/<int:id>", methods=['DELETE'])
    def delete_positions(id):
        return posicoes_controllers.delete(id)