from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    submit = SubmitField('Log In')

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    repassword = PasswordField('repassword', validators=[Required()])
    submit = SubmitField('Sign Up')
