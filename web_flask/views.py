from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, current_user
from models import storage
from models.task import Task


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

@views.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        # Process the form submission
        task_title = request.form.get('task_title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        due_date = request.form.get('due_date')
        user_id = current_user.id

        if len(description) < 5:
            flash('please give more detailed discription', category='error')
        elif len(task_title) < 2:
            flash('detailed title is required', category='error')
        elif due_date is None:
            flash('please set due date', category='error')
        else:
            new_task = Task(title=task_title, description=description, due_date=due_date, user_id=user_id)
            storage.new(new_task)
            storage.save()
            flash('New Task added Successfully', category='success')
            return redirect(url_for('views.tasks'))

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
