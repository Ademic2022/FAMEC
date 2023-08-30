from flask import Blueprint, render_template, url_for,request, flash, redirect
from models import storage
from models.user import User
import hashlib

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the form submission
        email = request.form.get('email')
        password = request.form.get('password')
        hash_password = hashlib.md5(password.encode()).hexdigest()

        user = storage.find_user_by_email(email)
        if user:
            if hash_password == user.password:
                flash('Logged in successfully', category='success')
                return redirect(url_for('views.dashboard'))
            else: 
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User with this email does not exist', category='error')

    return render_template('auth/login.html') 

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')
    # return render_template('login.html')