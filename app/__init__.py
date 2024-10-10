#!/usr/bin/python3

from flask import Flask
from app.db import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO
from app.config import Config


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Register blueprints
    from app.web_flask.routes import main as main_blueprint
    from app.web_dynamic.routes import dynamic as dynamic_blueprint
    from app.api.routes import api as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(dynamic_blueprint, uri_prefix='/dynamic')
    app.register_blueprint(api_blueprint, uri_prefix='/api')

    # Configure login
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'


    # App configurtion
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatwebapp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'i will input my seret_key'

    # Initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints
    from app.routes.user_routes import register
    register(app)


    return app
