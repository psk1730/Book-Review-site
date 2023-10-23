from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField, URLField, SelectField,FloatField
from wtforms.validators import Email, Length, EqualTo, DataRequired

class AdminRegistrationForm(FlaskForm):
    email= StringField("Email", validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField("Register")

class AdminLoginForm(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired(), Length(min= 6)])

    submit = SubmitField("Login")

class DoAddBook(FlaskForm):
    title= StringField("Title", validators=[DataRequired()] )
    isbn= IntegerField("ISBN", validators=[DataRequired()] )
    shoping= URLField("Shop Link",validators=[DataRequired()] )
    author= StringField("Author", validators=[DataRequired()] )
    gener= SelectField("Gener",validators=[DataRequired()])
    rate= FloatField("rating",validators=[DataRequired()])
    summary= StringField("This Summary", validators=[DataRequired()] )
    submit = SubmitField("Save")
