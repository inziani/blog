from flask import Flask, render_template
from config import config
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
pagedown = PageDown()
migrate = Migrate()

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  
  bootstrap.init_app(app)
  login_manager.init_app(app)
  db.init_app(app)
  csrf = CSRFProtect(app)
  pagedown.init_app(app)
  migrate.init_app(app, db)

    
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/auth')

  return app

from .main import views