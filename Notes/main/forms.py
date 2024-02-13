from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from Notes.models import User



class Search(FlaskForm):
	query = StringField('Search', validators=[DataRequired()])
	submit = SubmitField('Submit')


class Category(FlaskForm):
	category = SelectField('Filter by Category', choices = ['Text-Book', 'Notes', 'PYQs'], id='Category', validators=[DataRequired()])
	submit = SubmitField('Filter By')
