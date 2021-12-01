from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = '17ea8b95909637c15d7c3370f11d0825'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

from flaskblogdir import routes


