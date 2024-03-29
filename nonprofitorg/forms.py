from wtforms import StringField, PasswordField, SubmitField,HiddenField,TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField()

class TokenHiddenForm(FlaskForm):
    token = HiddenField("Token Hidden",id="token-hidden")
    submit = SubmitField()
 
class ContactForm(FlaskForm):
  name = StringField("Name")
  email = StringField("Email")
  subject = StringField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")