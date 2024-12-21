# backend/app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import main
    app.register_blueprint(main)

    return app
