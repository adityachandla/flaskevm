from flask import Blueprint
from mainapp import bootstrap,db


user = Blueprint("users",__name__, template_folder="templates")

import users.views