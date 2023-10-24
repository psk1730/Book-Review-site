from flask import Flask, render_template
from forms import AdminRegistrationForm, AdminLoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' # path to data base

db = SQLAlchemy(app)  # data base created
name ="pravesh kashyap"

# here we are converting table having three columns of different
# data type into code. 
class User(db.Model):   # create first intity 
    id = db.Column(db.Integer, primary_key = True)   # to tell that no two can have same id
    email = db.Column(db.String(60), nullable= False) # email can not be null
    password = db.Column(db.String(32), nullable = False)  

    def __reper__(self):
        return f"User(email: {self.email})"
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(120), nullable= False)  #title is must
    isbn = db.Column(db.Integer, unique= True, nullable= False)
    shop_link = db.Column(db.String(120), nullable= True)  #optional
    author = db.Column(db.String(60), nullable = False)
    gener = db.Column(db.String(60), nullable= False)
    rating= db.Column(db.Float, nullable= False)
    image = db.Column(db.String(120), nullable = True, default= "default.jpg")
    tiny_summry = db.Column(db.Text, nullable = False) # special type
   
    def __reper__(self):
        return f"Book(title: {self.title}, isbn:{ self.isbn})"


dict=  { "website_name":  "readaholic",
        "friend" : "PSK"} 

@app.route("/")
def home():
    return render_template("home.html", title = dict)

@app.route("/register", methods=["GET", "POST"])
def Adminregister():
    form = AdminRegistrationForm() # this is dynamic data so here it is pass through python
    if form.validate_on_submit:
        # print(form.data) data files created in terminal and print on validate
        _email= form.data['email'] # after filling form data goes to backend take that data add to data base
        _password= form.data['password'] # _email, _password are variable storing data coming from backend 
        user= User(email= _email, password=_password) # create user 
        db.session.add(user) # add user till now it is in ram 
        db.session.commit() # ram to data base
        print("user added")
    return render_template("register.html", form= form)

@app.route("/login", methods=["GET", "POST"])
def AdminLogin():
    form = AdminLoginForm()
    return render_template("login.html", form= form)
   

if __name__== "__main__":
    app.run(debug=True)