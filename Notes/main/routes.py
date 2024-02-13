from flask import Blueprint, render_template, request, Blueprint 
from flask import current_app
from Notes.models import Post
from Notes.main.forms import Search, Category

main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
	return render_template('home.html', title='Home')



#filter content by category in computer branch
@main.route("/category/computer", methods=['GET', 'POST'])
def compfilt():
	form = Category()
	posts = Post.query
	if form.validate_on_submit():		
		filter = form.category.data
		print(filter)
		posts = posts.filter_by(branch='Computer Science',category=filter).all()
		for post in posts:
			print(post.title)
		return  render_template('category.html', title='Computer Science', form=form, posts=posts, filter=filter)	



#filter content by category in electrical branch
@main.route("/category/electrical", methods=['GET', 'POST'])
def elecfilt():
	form = Category()
	posts = Post.query
	if form.validate_on_submit():		
		page = request.args.get('page', 1, type=int)		
		filter = form.category.data
		print(filter)
		posts = posts.filter_by(branch='Electrical',category=filter).paginate(page=page, per_page=4)
		for post in posts:
			print(post.title)
		return  render_template('category.html', title='Electrical', form=form, posts=posts, filter=filter)	



#filter content by category in mechanical branch
@main.route("/category/mechanical", methods=['GET', 'POST'])
def mechafilt():
	form = Category()
	posts = Post.query
	if form.validate_on_submit():
		page = request.args.get('page', 1, type=int)		
		filter = form.category.data
		print(filter)
		posts = posts.filter_by(branch='Mechanical',category=filter).paginate(page=page, per_page=4)
		for post in posts:
			print(post.title)
		return  render_template('category.html', title='Mechanical', form=form, posts=posts, filter=filter)	



#search content
@main.route("/search", methods=['GET','POST'])
def search():
	form = Search()
	posts = Post.query
	if form.validate_on_submit():	
		query = form.query.data
		posts = posts.filter(Post.title.like('%' + query + '%'))
		return render_template('search.html', title='Search', form=form, posts=posts)




# home page of computer branch		
@main.route("/computer", methods=['GET', 'POST'])
def computer():
	form = Category()
	page = request.args.get('page', 1, type=int)	
	posts = Post.query.filter_by(branch='Computer Science').paginate(page=page, per_page=4)
	return render_template('computer.html', title='Computer Science',posts=posts, form=form)



# home page of electrical branch
@main.route("/electrical", methods=['GET'])
def electrical():
	form = Category()
	page = request.args.get('page', 1, type=int)	
	posts = Post.query.filter_by(branch='Electrical').paginate(page=page, per_page=4)
	return render_template('electrical.html', title='Electrical', posts=posts, form=form)



# home page of mechanical branch
@main.route("/mechanical", methods=['GET'])
def mechanical():
	form = Category()
	page = request.args.get('page', 1, type=int)	
	posts = Post.query.filter_by(branch='Mechanical').paginate(page=page, per_page=4)
	return render_template('mechanical.html', title='Mechanical', posts=posts, form=form)



# about section
@main.route("/about")
def about():
	return render_template('about.html', title = "About")	
