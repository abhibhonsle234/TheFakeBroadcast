from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class NewsForm(FlaskForm):
	Headlines = TextField("Headlines", validators=[Length(max=30), DataRequired()])
	Description = TextAreaField("Description", validators=[Length(max=1000), DataRequired()])
	AuthorName = StringField("AuthorName", validators=[Length(max=20), DataRequired()])
	NewsCategory = SelectField("NewsCategory", choices=["General", "Lifestyle", "Travel", "Sports", "Crime"])
	Submit = SubmitField("Submit NewsCategory")

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        '''user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")'''
        pass