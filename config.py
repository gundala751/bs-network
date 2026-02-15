import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}