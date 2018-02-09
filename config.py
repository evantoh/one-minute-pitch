import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("evanmwenda@gmail.com")
    MAIL_PASSWORD = os.environ.get("evans123")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evans:evans123@localhost/one_minute_pitch'
    
    
class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evans:evans123@localhost/one_minute_pitch'
    DEBUG = True    

config_options = {
'development':DevConfig,
'production':ProdConfig
}