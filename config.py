from os import environ, path

class Config:
  SECRET_KEY ='98d704bf8b0febc605b80b105439fd17'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
  FLASK_ENV = 'development'

  @staticmethod
  def create_app():
    pass


class DevConfig(Config):
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
  

class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'

config = {
  'development' : DevConfig,
  'testing' : TestingConfig,
  'production' : ProdConfig,
  'default': DevConfig
}
