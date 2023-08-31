from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'famec'

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from models import storage
        return storage.find_user_by_id(id)

    return app  # Return the app instance here

# Configure the database session when the Flask app is created or initialized
def configure_db(app):
    from models import storage
    with app.app_context():
        storage.reload()
    return app

