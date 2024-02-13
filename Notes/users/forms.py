from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from Notes.models import User



class Registration(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])

	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ])

	submit = SubmitField('Signup')


	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()

		if user:
			raise ValidationError('The username is already taken. Please choose another username')

	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('There is already an account associated with this email.')



class Login(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')



class RequestReset(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])

	submit = SubmitField('Request Password Reset')


	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()

		if user is None:
			raise ValidationError('There is no account for this email. You must register first.')


class ResetPassword(FlaskForm):

	password = PasswordField('Password', validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ])

	submit = SubmitField('Reset Password')
