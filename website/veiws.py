from flask import Blueprint

# defining the routes
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1> Test </h1>"

# now register these blueprints in our init.py file
