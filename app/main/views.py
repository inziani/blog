from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user
from .forms import PostForm, CommentForm
from app.models import Post, User, Comment
from . import main
from .. import db
from .request import random_quotes


@main.route('/', methods=['GET', 'POST'])
def home():
  form=PostForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, category=form.category.data, content=form.content.data, 
    user_id=current_user.username) 
    db.session.add(post)
    db.session.commit()
    flash('Your Post has been created')
    return redirect(url_for('.home'))
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.category).paginate(page=page, per_page=5)
  daily_quotes = random_quotes()
  comments=Comment.query.order_by(Comment.timestamp.asc())#.paginate(page=page, per_page=5)) # Addition of comments
  return render_template('home.html', posts=posts, title='bloghome', form=form, daily_quotes=daily_quotes)


@main.route('/post/new', methods=['GET', 'POST'] )
@login_required
def new_post():
  form = PostForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, category=form.category.data, content=form.content.data, 
    user_id=current_user.username) 
    db.session.add(post)
    db.session.commit()
    flash('Your Post has been created')
    return redirect(url_for('.home'))
  return render_template('home.html', form=form, title='home')


@main.route('/post/delete/<int:posts_id>', methods=['GET', 'POST'] )
@login_required
def delete(posts_id):
  post = Post.query.get_or_404(posts_id)
  db.session.delete(post)
  db.session.commit()
  form = PostForm()
  return redirect(url_for('.home'))

@main.route('/edit/<int:posts_id>', methods=['GET', 'POST'] )
@login_required
def edit(posts_id):
  form = PostForm()
  post = Post.query.get_or_404(posts_id)
  if form.validate_on_submit:
    post.content = form.content.data
    db.session.add(post)
    flash('The post has been updated')
    return redirect(url_for('.home', posts_id=posts_id))
  form.body.content = post.content
  return render_template('edit.html', form=form)
  

  @main.route('/post/<int:posts_id>', methods=['GET', ['POST']])
  @login_required
  def post_comment(posts_id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
      comment = Comment(comment=form.comment.data, post_id=post_id, user_id=current_user.username)
      db.session.add(comment)
      db.session.commit()
      flash('Your comment has been posted')
      return redirect(url_for('.post', posts_id=posts.id))
    comments = post.comment.query_all()
    return render_template('comments.html', post=post, form=form, title='Comment')

  @main.route('/user_account/<string:username>', methods=['GET', ['POST']])
  @login_required
  def user_account(username):
    post = Post.query.get_or_404(username)
    form = CommentForm()
    if form.validate_on_submit():
      comment = Comment(comment=form.comment.data, post_id=post_id, user_id=current_user.username)
      db.session.add(comment)
      db.session.commit()
      flash('Your comment has been posted')
      return redirect(url_for('.post', posts_id=posts.id))
    comments = post.comment.query_all()
    return render_template('comments.html', post=post, form=form, title='Comment')

  @main.route('/animals', methods=['GET', 'POST'])
  def animals():
    form=PostForm()
    if form.validate_on_submit():
      post = Post(title=form.title.data, category=form.category.data, content=form.content.data, 
      user_id=current_user.username) 
      db.session.add(post)
      db.session.commit()
      flash('Your Post has been created')
      return redirect(url_for('.home'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.category).paginate(page=page, per_page=5)
    daily_quotes = random_quotes()
    comments=Comment.query.order_by(Comment.timestamp.asc())#.paginate(page=page, per_page=5)) # Addition of comments
    return render_template('home.html', posts=posts, title='bloghome', form=form, daily_quotes=daily_quotes)
