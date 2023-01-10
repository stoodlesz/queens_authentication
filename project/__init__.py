from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets  # Generate cryptographically strong pseudo-random numbers suitable for managing secrets such as
# account authentication, tokens, and similar.

secret_key = secrets.token_hex(16)  # implement a hex for a secret key to hash the passwords

# initialise SQLAlchemy, use it later in the models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for authentication routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-authentication parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
