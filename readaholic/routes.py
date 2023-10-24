from flask import render_template
from readaholic.forms import AdminRegistrationForm, AdminLoginForm
from readaholic.models import User
from readaholic import app
from readaholic import db

@app.route("/")
def home():
    return render_template("home.html", title = dict)

@app.route("/register", methods=["GET", "POST"])
def Adminregister():
    form = AdminRegistrationForm() # this is dynamic data so here it is pass through python
    if form.validate_on_submit:
        print(form.data) #data files created in terminal and print on validate    
        _email= form.data['email']
        _password= form.data['password']
        user= User(email= _email, password= _password)
        db.session.add(user)
        db.session.commit()
    return render_template("register.html", form= form)

@app.route("/login", methods=["GET", "POST"])
def AdminLogin():
    form = AdminLoginForm()
    return render_template("login.html", form= form)