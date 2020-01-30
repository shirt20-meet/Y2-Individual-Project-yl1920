from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session
from database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'shir'

@app.route('/', methods = ["GET"])
def home():
	return render_template("home.html")

@app.route('/addPlace',methods=['GET', 'POST'])
def addPlace():
	if request.method == "GET":
		return render_template("addPlace.html")

	else:
		add_place(request.form['name'], request.form['country'], request.form['city'], request.form['street'])
		return render_template("home.html")

@app.route('/api',methods=['GET','POST'])
def api():
	places_list = query_all()
	return render_template('api.html', places=places_list)

if __name__ == '__main__':
	app.run(debug=True)