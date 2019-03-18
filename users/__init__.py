from flask import Blueprint
from mainapp import bootstrap,db


user = Blueprint("users",__name__, template_folder="templates", static_folder="static",
	static_url_path="/users/static")

import users.views