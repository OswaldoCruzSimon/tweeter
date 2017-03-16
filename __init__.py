from flask import Flask
from flask import render_template
from flask import request

#import manageTweet

app = Flask(__name__)#,template_folder='template')

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}  # fake user
	return render_template('index.html',
						   title='Home',
						   user=user)
"""
@app.route('/base')
def base():
	user = {'nickname': 'Miguel'}
	posts = [
	{
		'author': {'nickname': 'John'}, 
		'body': 'Beautiful day in Portland!' 
	},
	{ 
		'author': {'nickname': 'Susan'}, 
		'body': 'The Avengers movie was so cool!' 
	}
	]
	return render_template('/inheritance.html',
							title='Home',
							user=user,
							posts=posts)
"""

@app.route('/chart',methods=['GET', 'POST'])
def chart():
	name ='data.tsv'
	sel = request.args.get('sel')
	filtro = request.args.get('filtro')

	#manageTweet = ManageTweet()
	#data = manageTweet.getCantTweet(banco, fecha_ini,fecha_fin,filtro)
	print("params: %s %s"%(sel,filtro))
	print(data)
	return render_template('chart.html',
							name=name)
