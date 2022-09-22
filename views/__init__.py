from flask import Blueprint

sugg_blue = Blueprint('suggestion', __name__, url_prefix='/suggestion')

from views.sug_views import heros
