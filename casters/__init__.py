from mainapp import db,bootstrap
from flask import Blueprint


caster = Blueprint("caster",__name__,template_folder="templates",static_url_path="/casters/static",static_folder="static")

import casters.views