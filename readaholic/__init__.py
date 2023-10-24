from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key_33'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///base.db' # path to data base

db = SQLAlchemy(app)  # data base created

import readaholic.routes # earlier routes were just below data base 
                         # to import routes in app import routes here