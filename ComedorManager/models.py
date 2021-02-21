from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, DateTime
)
from ComedorManager import db


def save_item(item):
    db.session.add(item)
    db.session.commit()


class Comedor(db.Model):
    id = Column(Integer, primary_key=True)
    empresa = Column(String(40), nullable=False)
    semana = Column(DateTime, nullable=False, default=datetime.utcnow)
    gastos = Column(Integer, nullable=False, default=0)
    ventas = Column(Integer, nullable=False, default=0)
    impuesto = Column(Integer, nullable=False, default=0)
    total = Column(Integer, nullable=False, default=0)

    
    def __repr__(self):
        return self.__dict__
