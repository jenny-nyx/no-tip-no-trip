from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'meowmeow' # encrypt and secure cookies and session data

    from .views import views
    # If we wanted /meow/home - then the url_prefix would be /meow. This is where we register blueprints for all these different parts
    app.register_blueprint( views, url_prefix='/')

    return app