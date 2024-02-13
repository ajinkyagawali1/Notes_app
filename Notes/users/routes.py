from flask import Blueprint 
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from Notes import db, bcrypt
from Notes.models import User, Post
from Notes.users.forms import (Registration, Login,
                                   RequestReset, ResetPassword)
from Notes.users.utils import send_reset_email 



users = Blueprint('users', __name__)



#user registration
@users.route("/register", methods=['GET', 'POST'])
def register():
	form = Registration()
	if current_user.is_authenticated:
		return redirect(url_for('users.login'))
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('users.login'))

	return render_template('register.html', title='Register', form = form)


# user login
@users.route("/login", methods=['GET', 'POST'])
def login():
	form = Login()
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			flash(f'{form.email.data} is successfully logged in!', 'success')
			return redirect(next_page) if next_page else redirect(url_for('users.login'))
		else:
			flash('Login Unsuccessful. Please check email and password and try again.', 'danger')
	return render_template('login.html', title='Login', form = form)


# logout
@users.route("/logout")
def logout():
	logout_user()
	flash(f'You have successfully logged out', 'success')
	return redirect(url_for('main.home'))

# account
@users.route("/account")
@login_required
def account():
	return render_template('account.html', title='Account')

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('users.login'))

	form = RequestReset()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent with instructions to reset password.' , 'info')
		return redirect(url_for('users.login'))
	return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
	if current_user.is_authenticated:
		return redirect(url_for('users.login'))

	user = User.verify_reset_token(token)

	if user is None:
		flash('That is an invalid or expired token!', 'warning')
		return redirect(url_for('users.reset_request'))

	form = ResetPassword()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user.password = hashed_pw
		db.session.commit()
		flash('Your has password been updated! You are now able to log in.', 'success') 
		return redirect(url_for('users.login'))
	return render_template('reset_password.html', title='Reset Password', form = form)
