from readaholic import db


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