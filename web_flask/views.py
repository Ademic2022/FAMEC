from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)


"""Route to Landing PAGE"""
@views.route('/')
def landing_page():
    background_image_urls = [
        url_for('static', filename='images/home1.jpg'),
        url_for('static', filename='images/home2.jpg'),
        url_for('static', filename='images/home3.jpg'),
        url_for('static', filename='images/hma_banner.jpg'),
        url_for('static', filename='images/hma3.jpg'),
        url_for('static', filename='images/hma1.jpg'),
        url_for('static', filename='images/about.jpg')
    ]
    return render_template('landing_page.html', images = background_image_urls)

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

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
