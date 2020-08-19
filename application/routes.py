import os
import io
from application import app
from flask import render_template, session, flash, json, redirect, url_for
from application.forms import NewsForm 
from application.forms import LoginForm, RegisterForm

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static", "users.json")

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	print(json_url)
	if os.path.isfile(json_url) and os.access(json_url, os.R_OK):
		print ("File exists and is readable")
	else:
		print ("Either file is missing or is not readable, creating file...")
		with io.open(json_url, 'w+') as db_file:
			db_file.write(json.dumps({})) 
	with open(json_url) as user_file:
		data = json.load(user_file)
		print("users.json", data)
	return render_template("index.html", index=True )

@app.route("/login", methods=['GET','POST'])
def login():
	if session.get('username'):
		return redirect(url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		with open(json_url) as user_file:
			data = json.load(user_file)
			if data.get(email):
				user = data.get(email)
				print(user.keys())
				if password == user["password"]:
					flash(f"{user['first_name']}, you are successfully logged in!", "success")
					session['user_id'] = user["user_id"]
					session['username'] = user["first_name"]
					return redirect("/index")
				else:
					flash("Sorry, something went wrong.","danger")	
			else:
				flash("Sorry, something went wrong.","danger")
	return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
	session["user_id"] = False
	session.pop('username', None)
	return(url_for("index"))

@app.route("/register", methods=['POST','GET'])
def register():
	if session.get('username'):
		return redirect(url_for('index'))

	form = RegisterForm()
	if form.validate_on_submit():
		with open(json_url) as user_file:
			data = json.load(user_file)
			user_id = len(data.keys())
			user_id += 1
			email = form.email.data
			password = form.password.data
			first_name = form.first_name.data
			last_name = form.last_name.data
			user = {"user_id":user_id, "email":email, "password":password, "first_name":first_name, "last_name":last_name}
			data[email] = user
			
			print("users.json", data)
			flash("You are successfully registered!","success")
		
		with io.open(json_url, 'w+') as db_file:
			db_file.write(json.dumps(data))

		return redirect(url_for('index'))

	return render_template("register.html", title="Register", form=form, register=True)

@app.route('/news')
def news():
	return render_template("news.html", news=True)

@app.route('/contact_us')
def contact_us():
	return render_template("contact_us.html", contact_us=True)

@app.route('/add_news')
def add_news():
	form = NewsForm()
	return render_template("add_news.html", form=form)