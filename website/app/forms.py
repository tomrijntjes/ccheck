from flask import flash
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, StringField
from wtforms.validators import DataRequired, Length
from .models import db, User

class SignupForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create account")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
      return False

    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      flash("That email is already taken", "warning")
      return False
    else:
      return True

class LoginForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
      return False

    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      flash("Invalid e-mail or password", "warning")
      return False

class Email1(Form):
    template1 = StringField('Template1', validators=[DataRequired()])
    template2 = StringField('Template2', validators=[DataRequired()])
    template3 = StringField('Template3', validators=[DataRequired()])
    template4 = StringField('Template4', validators=[DataRequired()])
    template5 = StringField('Template5', validators=[DataRequired()])
    submit = SubmitField("Save changes")

class Email2(Form):
    template1 = StringField('Template1', validators=[DataRequired()])
    template2 = StringField('Template2', validators=[DataRequired()])
    template3 = StringField('Template3', validators=[DataRequired()])
    template4 = StringField('Template4', validators=[DataRequired()])
    template5 = StringField('Template5', validators=[DataRequired()])
    submit = SubmitField("Save changes")

class Email3(Form):
    template1 = StringField('Template1', validators=[DataRequired()])
    template2 = StringField('Template2', validators=[DataRequired()])
    template3 = StringField('Template3', validators=[DataRequired()])
    template4 = StringField('Template4', validators=[DataRequired()])
    template5 = StringField('Template5', validators=[DataRequired()])
    submit = SubmitField("Save changes")
