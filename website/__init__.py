# setup flask
from flask import Flask


# initialize flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'sdfkjshdfhakjskjk'
    # add blueprints
    from .veiws import views
    from .auth import auth

    # register them
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
