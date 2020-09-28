from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError


class PostForm(FlaskForm):
  title = StringField('Title', validators=[Required()])
  category = StringField('Category', validators=[Required()])
  content = TextField("whas'up?", validators=[Required(), Length(1, 20, message='Your pitch is too long')])
  SubmitField = SubmitField('Post')

class CommentForm(FlaskForm):
  content = StringField('Comment' , validator=[Required()])
  submit = SubmitField('Submit')