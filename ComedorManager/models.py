import click
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, DateTime
)
from flask.cli import with_appcontext
from ComedorManager import db


def save_item(item):
    db.session.add(item)
    db.session.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.drop_all()
    db.create_all()
    click.echo('Initialized database')


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
