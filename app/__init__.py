from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

db = SQLAlchemy()

def create_app(config_class=DevConfig):
    """ 
    Creates an application instance to run using settings from config.py 
    :return: A Flask object 
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialise the database and create tables 
    db.init_app(app)
    from app.models import User, City, Forecast
    with app.app_context():
        db.create_all()

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app