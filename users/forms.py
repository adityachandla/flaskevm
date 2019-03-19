from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email

class SignIn(FlaskForm):
	username = StringField("Enter your username", validators=[DataRequired()])
	password = PasswordField("Enter your password", validators=[DataRequired()])
	submit = SubmitField("Vote")


class SignUp(FlaskForm):
	username = StringField("Enter your username", validators=[DataRequired()])
	password = PasswordField("Enter your password", validators=[DataRequired()])
	password2 = PasswordField("Enter your password again", validators=[DataRequired()])
	email = StringField("Ente your email address", validators=[DataRequired(),Email()])
	submit = SubmitField("Join")