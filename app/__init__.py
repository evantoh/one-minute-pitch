from flask import  Flask 
from flask_bootstrap import Bootstrap
from config import config_options
#initializing the application


bootstrap = Bootstrap()

def create_app(config_name):
    
app = Flask(__name__)   


#creating the app configurations
app.config.from_object(config_options[config_name])

#initilising flask extensions
bootstrap.init_app(app)

#registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app 