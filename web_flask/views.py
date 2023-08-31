from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

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
@login_required
def users():
    return render_template('users.html', user = current_user)

@views.route('/tasks')
@login_required
def tasks():
    return render_template('task.html', user = current_user)

@views.route('/notification')
@login_required
def notification():
    return render_template('notification.html', user = current_user)

@views.route('/events')
@login_required
def events():
    return render_template('events.html', user = current_user)

@views.route('/family')
@login_required
def family():
    return render_template('family.html', user = current_user)

@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user = current_user)
