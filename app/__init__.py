from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config  # Import the Config class directly

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes.auth_routes import auth_bp
    from .routes.student_routes import student_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)

    return app
