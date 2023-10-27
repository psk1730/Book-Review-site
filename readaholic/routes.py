from flask import render_template, flash, redirect, url_for, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from readaholic.forms import AdminRegistrationForm, AdminLoginForm, AdminAddBooksForm, AdminCommentForm
from readaholic import db, app, bcrypt
from readaholic.models import User, Comment, Book
import os
from uuid import uuid4

@app.route("/")
@login_required
def home():
    book_data = Book.query.all()
    return render_template("home.html", data=book_data) 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET","POST"])
def register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        user = User(email=_email, password=_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account successfully created, you may now login","success") 
            return redirect(url_for("login"))
        except:
            flash("Something went wrong with database","warning")
        # print("registered")
    return render_template("register.html",form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!","success")
        return redirect(url_for('home'))
    
    form = AdminLoginForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first()
        if not user:
            flash(f"No user with email{_email} found! Register today.","danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                login_user(user)
                flash("Successfully logged in!","success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!","danger")
    return render_template("login.html",form=form)

@app.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out","success")
    return redirect(url_for("login"))

def save_cover_image(cover_image):
    f = cover_image.data
    filename = f"picture-{str(uuid4())}.{f.filename.split('.')[1].lower()}"
    f.save(os.path.join(app.instance_path, "uploads", filename))
    return filename


@app.route("/books", methods=["GET","POST"])
@login_required
def books():
    form = AdminAddBooksForm()
    if form.validate_on_submit():
        _title = form.data['title']
        _author = form.data['author']
        _isbn = form.data['isbn']
        _genre = form.data['genre']
        _shop_link = form.data['shop_link']
        _rating = form.data['rating']
        cover_image_file = save_cover_image(form.cover_image_file)
        _tiny_summary = form.data['tiny_summary']
        book = Book(title=_title, author=_author,
                     isbn=_isbn, genre=_genre, 
                     shop_link=_shop_link, 
                     rating=_rating, 
                     tiny_summary=_tiny_summary,
                    image=cover_image_file)
        try:
            db.session.add(book)
            db.session.commit()
            flash("Book info added","success")
        except:
            flash("Something went wrong while adding the book information","danger")
        # print("Book info added")
        # print(form.data)
    return render_template("book.html",form=form)

@app.route("/uploads/<filename>")   # upload the image having name as filename
def send_image_file(filename):
    return send_from_directory(os.path.join(app.instance_path, "uploads"), filename)


@app.route("/comment", methods=["GET","POST"])
def comment():
    form = AdminCommentForm()
    if form.validate_on_submit():
        _name = form.data['name']
        _email = form.data['email']
        _comment = form.data['comment']
        comment = Comment(name=_name, email=_email, comment=_comment)
        db.session.add(comment)
        db.session.commit()
        print(" comment added")
    return render_template("comment.html",form=form)

@app.route("/book/<isbn>", methods=["GET"])
def get_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        flash("Book not found")
        return redirect(url_for('home'))
    else:
        return render_template("book.html", data=book)