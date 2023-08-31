from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user, logout_user, login_user


views = Blueprint('views', __name__)


"""Route to Landing PAGE"""
@views.route('/')
def landing_page():
    background_image_urls = [
        url_for('static', filename='images/home1.jpg'),
        url_for('static', filename='images/home2.jpg'),
        url_for('static', filename='images/home3.jpg'),
        url_for('static', filename='images/about.jpg'),
        url_for('static', filename='images/Famec_logo_white.png')
    ]
    return render_template('landing_page.html', images = background_image_urls)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user = current_user)

@views.route('/users')
def users():
    return render_template('users.html')

@views.route('/tasks')
def tasks():
    return render_template('task.html')

@views.route('/notification')
def notification():
    return render_template('notification.html')

@views.route('/events')
def events():
    return render_template('events.html')

@views.route('/family')
def family():
    return render_template('family.html')

@views.route('/settings')
def settings():
    return render_template('settings.html')
