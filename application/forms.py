from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class NewsForm(FlaskForm):
	Headlines = StringField("Headlines", validators=[Length(max=30), DataRequired()])
	Description = StringField("Description", validators=[Length(max=1000), DataRequired()])
	AuthorName = StringField("AuthorName", validators=[Length(max=20), DataRequired()])
	NewsCategory = SelectField("NewsCategory", choices=["General", "Lifestyle", "Travel", "Sports", "Crime"])
	Submit = SubmitField("Submit NewsCategory")
