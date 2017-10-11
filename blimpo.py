from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for, flash

#set default user/password for testing
defaultUser = "Bob"
defaultPassword = "123" 

#create the app and add a session/cookie
app=Flask(__name__)
app.secret_key=urandom(32)

@app.route('/')
def root():
    #render loggedIn page if session has "user":"Bob"
    if 'user' in session:
		if session['user']=='Bob':
			return redirect(url_for("welcome"))
    #otherwise, render login page
    else:
        return redirect(url_for("login"))

@app.route("/entry", methods=["GET", "POST"])	      
def entry():
    #if correct info is entered thru form, store session, and render loggedIn page
    if (request.form["username"]=="Bob") and (request.form["password"]=="123"):
        session["user"] = "Bob"
        return redirect(url_for("welcome"))
    #otherwise if username/password combo is wrong, render error page
    else:
		if request.form["username"]!="Bob":
			flash("Wrong user")
		if request.form["password"]!="123":
			flash("Wrong password")
		return redirect(url_for("login"))

@app.route("/logOff", methods=["GET", "POST"])
def logOff():
    #if logoff button is hit, remove session, and render logoff page
    if 'user' in session:
        session.pop('user')
    return redirect(url_for("login"))
        

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login')
def login():
    return render_template("login.html")
    


if __name__ == '__main__':
    app.debug==True
    app.run()	
