from Notes import create_app, create_doc_dir, db



app = create_app()

if __name__ == '__main__':
	app.run(debug=True)

with app.app_context():
    db.create_all()

create_doc_dir()


