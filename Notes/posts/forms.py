from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class Upload(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])

	branch = SelectField('Select Branch', choices=['Computer Science', 'Electrical', 'Mechanical'],id = 'Branch', validators=[DataRequired()])

	category = SelectField('Select Category', choices=['Text-Book', 'Notes', 'PYQs'],id = 'Category', validators=[DataRequired()])
	
	file = FileField('Upload File', validators=[DataRequired(),FileAllowed(['pdf'])])
	
	submit = SubmitField('Upload')
