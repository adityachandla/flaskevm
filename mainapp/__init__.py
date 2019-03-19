from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os


base_dir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config["SECRET_KEY"] = "ANSJFB3232JDNA"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+base_dir+"/hello.db"


bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from users import user as user_blue
from casters import caster as cast_blue


app.register_blueprint(user_blue)
app.register_blueprint(cast_blue)

