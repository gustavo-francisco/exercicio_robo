from sqlalchemy import Column, Integer, Float
from src.models.base import Base
class Posicoes(Base):
    __tablename__ = "Posicoes"
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column (Float)
    z = Column (Float)
    j1 = Column(Float)
    j2 = Column(Float)
    j3 = Column(Float)

    def __repr__(self):
            return f"Posicoes(id={self.id!r}, x={self.x!r}, y={self.y!r}, z={self.z!r}), j1={self.j1!r}, j2={self.j2!r}, j3={self.j3!r}"
    
    def return_json(self):
          return {
                'id': self.id,
                'x': self.x,
                'y': self.y,
                'z': self.z,
                'j1': self.j1,
                'j2': self.j2,
                'j3': self.j3
          }