from flask import Flask
from flaskext.mysql import MySQL
from config import app_config

db = MySQL()

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Muff4hire'
    app.config['MYSQL_DATABASE_DB'] = 'uranium_database'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    db.init_app(app)

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app
