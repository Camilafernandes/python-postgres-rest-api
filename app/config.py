#!/usr/bin/env python
import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from common.extensions import cache

app = Flask(__name__)
cache.init_app(app)

config_obj = yaml.load(open('config.yaml'), Loader=yaml.Loader)

# override the environment variables
database_url = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = config_obj['SQLALCHEMY_DATABASE_URI'] if database_url is None else database_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

### swagger specific ###
SWAGGER_URL = '/'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
