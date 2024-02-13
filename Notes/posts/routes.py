from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, send_file)
from flask_login import current_user, login_required
from Notes import db
from Notes.models import Post
from Notes.posts.forms import Upload
from Notes.users.utils import save_file


posts = Blueprint('posts', __name__)



@posts.route("/new", methods=['GET', 'POST'])
@login_required
def new():
	form = Upload()
	if form.validate_on_submit():
		if form.file.data:
			filename, file_path = save_file(form.file.data, form.title.data)	
			post = Post(title = form.title.data, path = file_path, branch = form.branch.data, category = form.category.data, author=current_user)
			db.session.add(post)
			db.session.commit()
		print(form.file.data)
		flash(f'You successfully uploaded a file!', 'success')
		return redirect(url_for('main.home'))
	return render_template('new_post.html', title='Upload File', form = form)


#download file
@posts.route("/download", methods=['GET', 'POST'])
def download():
	file = request.args.get('file')
	return send_file(file, as_attachment=True)
