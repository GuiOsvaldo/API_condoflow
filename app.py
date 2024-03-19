from flask import Flask 
from extensions import api, db
from resources import ns


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Angola2023#@102.219.126.14:5432/condoflow_db'    
    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app