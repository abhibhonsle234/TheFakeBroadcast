from application import app
from flask import render_template
from application.forms import NewsForm 

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

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