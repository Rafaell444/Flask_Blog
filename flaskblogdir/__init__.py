from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)

app.config["SECRET_KEY"] = '17ea8b95909637c15d7c3370f11d0825'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "users.login"

login_manager.login_message_category = "info"

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "raforafo26@gmail.com"
app.config["MAIL_PASSWORD"] = "dpstvcfwwwcppzvy"
mail = Mail(app)

from flaskblogdir.users.routes import users
from flaskblogdir.posts.routes import posts
from flaskblogdir.main.routes import main
from flaskblogdir.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)


