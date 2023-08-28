from flask import Blueprint, render_template, url_for
from models import storage

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')
    # return render_template('login.html')