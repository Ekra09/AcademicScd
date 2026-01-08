from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config  # Import the Config class directly
import os

from flask import redirect, url_for
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    instance_path = os.environ.get("FLASK_INSTANCE_PATH", os.path.join(os.sep, "tmp", "instance"))
    app = Flask(__name__, instance_path=instance_path)
    app.config.from_object(Config)  # Load configuration from Config class

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        db.create_all()

    from .routes.auth_routes import auth_bp
    from .routes.student_routes import student_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)

    return app
