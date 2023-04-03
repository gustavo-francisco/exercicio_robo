
from src.config.db import session
from src.models.posicoes import Posicoes
from src.config import db
from flask import request

def read():
    positions = session.query(Posicoes).all()
    return str(positions)

def create():
    added_position = Posicoes(x = request.json['x'], y = request.json['y'], z = request.json['z'], j1 = request.json['j1'], j2 = request.json['j2'], j3 = request.json['j3'])
    session.add(added_position)
    session.commit()
    return added_position.return_json()

def update(id):
    position = session.query(Posicoes).filter_by(id=id).first()
    if position:
        new_position = request.json
        position.x = new_position['x']
        position.y = new_position['y']
        position.z = new_position['z']
        position.j1 = new_position['j1']
        position.j2 = new_position['j2']
        position.j3 = new_position['j3']
        session.commit()
        return 'Posição Atualizada!'
    else:
        return 'Posição Não encontrada!'
    
def delete(id):
    position = session.query(Posicoes).filter_by(id=id).first()
    db.session.delete(position)
    session.commit()
    return f"Posição {position.id} Excluída!"

