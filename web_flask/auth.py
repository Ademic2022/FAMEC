from flask import Blueprint, render_template, url_for,request
from models import storage
from models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     new_user = User(id = "fk", email = "hasfat@gmail.com", password = "12345", username = "kenny01")
    #     storage.new(new_user)
    #     storage.save()
    return render_template('auth/login.html')

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')
    # return render_template('login.html')