from flask import Blueprint, render_template, url_for,request, flash, redirect
from flask_login import login_required, current_user
from models import storage
from models.user import User
import hashlib
import re

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
                # flash('Logged in successfully', category='success')
                return redirect(url_for('views.dashboard'))
            else: 
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User with this email does not exist', category='error')

    return render_template('auth/login.html') 

# REGISTER ROUTE FUNCTIONALITY
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # action = request.form.get('register')
        # if action == 'register':
        user_data = {
            "firstname": request.form.get('firstname'),
            "lastname": request.form.get('lastname'),
            "username": request.form.get('username'),
            "password": request.form.get('password'),
            "confirm_pass": request.form.get('confirm_pass'),
            "email": request.form.get('email'),
            "address": request.form.get('apt'),
            "apt": request.form.get('apt'),
            "country": request.form.get('country'),
            "state": request.form.get('state'),
            "birth_month": request.form.get('birth_month'),
            "birth_day": request.form.get('birth_day'),
            "t_c": request.form.get('t_c')
        }

        if len(user_data['firstname']) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif len(user_data['lastname']) < 2:
            flash('Last Name must be greater than 1 character', category='error')
        elif user_data['password'] != user_data['confirm_pass']:
            flash('Passwords do not match', category='error')
        elif len(user_data['password']) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_data['email']):
            flash('Invalid email address', category='error')
        elif 't_c' not in user_data:
            flash('You must accept the terms and conditions to register', category='error')
        elif any(not user_data[field] for field in ['firstname', 'lastname', 'password', 'confirm_pass', 'email', 'address', 'apt', 'country', 'state', 'birth_month', 'birth_day']):
            flash('All fields are required', category='error')
        else:
            # All checks passed, proceed with registration
            flash('Registration successful', category='success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')
