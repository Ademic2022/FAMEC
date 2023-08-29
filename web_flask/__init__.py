from flask import Flask
from .views import views
from .auth import auth
from models import storage

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'famec'


    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app
def config_db(app):
    with app.app_context():
        storage.reload()
    return app