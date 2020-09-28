from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from flask_login import login_user, login_required, current_user
from .forms import PostForm, CommentForm
from app.models import Post, User, Comment
from . import main
from .. import db


@main.route('/')
def home():
  return render_template('home.html', title='bloghome')