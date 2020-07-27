from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index(): 
	user = {'username': 'Cameron'}
	posts = [
		{
			'author': {'username' : 'John'},
			'body': 'Beautiful day in London'
		
		},
		{
			'author' : {'username' : 'Dave'},
			'body' : 'Great day at the movies'
		}
	]
	return render_template('index.html', title='Home', user=user, posts = posts)