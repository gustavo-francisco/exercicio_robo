from flask import Flask
from src.config import db
from src.routes import posicoes_routes

def create_app():
    app = Flask(__name__)
    db

    posicoes_routes.init_app(app)
    return app