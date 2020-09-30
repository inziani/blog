from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, current_user, LoginManager, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
          flash('Invalid email or password')
          return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', title='Sign In', form=form)
  

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out')
  return redirect(url_for('main.home'))

@auth.route('/register', methods = ['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    password_hash = generate_password_hash(form.password.data, method='sha256')
    user = User(username = form.username.data, email=form.email.data,  password_hash = password_hash)
    db.session.add(user)
    db.session.commit()
    flash('Log in with your new credentials')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', form=form)