from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.instance_path}/my_db.sqlite"

    db.init_app(app)

    with app.app_context():
        from . import models

    from . import comedor
    app.register_blueprint(comedor.bp)

    return app
