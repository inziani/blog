from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField, SelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError 
from flask_pagedown.fields import PageDownField


class PostForm(FlaskForm):
  title = StringField('Title', validators=[Required()])
  category = SelectField('Category', choices=[("Crops", "Crops"),("Animals","Animals"), ("Agri-business","Agri-business" )], validators=[Required()])
  # content = TextAreaField("Content",  validators=[Required()])
  content = PageDownField("Content",  validators=[Required()])
  post = SubmitField('Post')
  
  

class CommentForm(FlaskForm):
  content = StringField('Comment' , validator=[Required()])
  submit = SubmitField('Submit')