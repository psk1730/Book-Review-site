from flask import Flask, render_template
from forms import AdminRegistrationForm

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'


name ="pravesh kashyap"

app= Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'

dict=  { "website_name":  "readaholic",
        "friend" : "PSK"} 

@app.route("/")
def home():
    
    return render_template("home.html", title = dict)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegistrationForm() # this is dynamic data so here it is pass through python
    return render_template("adminregister.html", form= form)
   

if __name__== "__main__":
    app.run(debug=True)