#Code for App Framework
#References: Tour-De-City (Previous Flask Framework Implemented by David Cahn)

from flask import Flask, render_template, request, redirect, session, url_for
from py import *
import json

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route("/", methods = ["GET","POST"])
def index():
	return render_template("index.html")

@app.route ("/input",  methods = ["GET","POST"])
def input():
	if request.method == "GET":
		print ("get")
	else: 
		print("post request")
		button = request.form['button'] if 'button' in request.form else None
		print (button)
		if button == "Submit":
			session['description'] = request.form.get("description", None)
			session['option_1'] = request.form.get("option1", None)
			session['option_2'] = request.form.get("option2", None)
			return redirect('/results')
	return render_template("input.html")

@app.route ("/results",  methods = ["GET","POST"])
def results():
    if ('description' in session.keys() and 'option_1' in session.keys() and "option_2" in session.keys()):
    	return render_template("results.html",dscr=session["description"],optn1=session["option_1"],optn2=session["option_2"])
    else:
    	return redirect('/')
	return render_template("results.html")

@app.route("/logout")
def logout():
	if "google_user_dict" in session.keys():
		session.pop("google_user_dict")
	return redirect(url_for("index"))

@app.route("/googleoauth", methods = ["POST"])
def googleoauth():
	session["google_user_dict"] = request.json
	return ""

@app.errorhandler(404)
def error400(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error500(error):
    return render_template("errors/500.html"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)