from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

class AddCreditsForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    credits = IntegerField('credits', validators=[Required()])
    submit = SubmitField('Add Credits')
