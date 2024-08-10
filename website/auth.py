from flask import Blueprint

# defining the routes
auth = Blueprint('auth', __name__)

# defining login,logout,etc authentication


@auth.route("/login")
def login():
    return "<p>login</p>"


@auth.route("/logout")
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>sign-up</p>"
