import random, hashlib, os
from flask import Flask, render_template, request, session

#set default user/password for testing
defaultUser = "Bob"
defaultPassword = "123" 

#create the app and add a session/cookie
app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/',methods=["GET","POST"])
def root():
	#render loggedIn page if session has "user":"Bob"
	if len(session)==1 and  session["user"]=="Bob":
		return render_template("loggedIn.html")
        #otherwise, render login page
	else:
                return render_template("login.html")

@app.route("/entry", methods=["GET", "POST"])	      
def entry():
        #if correct info is entered thru form, store session, and render loggedIn page
        if (request.form["username"]=="Bob") and (request.form["password"]=="123"):
                session["user"] = "Bob"
                return render_template("loggedIn.html")
        #otherwise if username/password combo is wrong, render error page
        else:
                return render_template("error.html")

@app.route("/logOff", methods=["GET", "POST"])
def logOff():
        #if logoff button is hit, remove session, and render logoff page
        session.pop("user")
        return render_template("loggedOff.html")
        

if __name__ == '__main__':
	app.debug==True
	app.run()	

	
