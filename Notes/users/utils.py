import os
import secrets
from flask import current_app, url_for
from flask_mail import Message
from Notes import mail
from Notes.main.forms import Search


#upload a new file
def save_file(file, title):
	f_name, f_ext = os.path.splitext(file.filename)
	f_name = title + f_ext
	file_path = os.path.join(current_app.root_path, 'static/docs', f_name)
	file.save(file_path)
	return f_name, file_path

# pass variables to the layout template
@current_app.context_processor
def base():
	form = Search()
	return dict(form=form)


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password reset request', sender='noreply@notes.com', recipients=[user.email])
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_password', token=token, _external=True)}
If you did not make this request then simply ignore this message, no changes will be done
'''
	mail.send(msg)
