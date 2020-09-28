#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Post, Comment
from flask_script import Shell, Manager
from flask_migrate import MigrateCommand
from flask_wtf.csrf import CsrfProtect, CSRFError

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)

@manager.shell
def make_shell_context():
  return dict(app=app, db=db, User=User, Post=Post, Comment=Comment)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
  manager.run()