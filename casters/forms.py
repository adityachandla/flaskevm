from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField,TextAreaField
from wtforms.validators import DataRequired




def getForm(q):
	class OptionForm(FlaskForm):
		option1 = BooleanField(q.option1)
		option2 = BooleanField(q.option2)
		option3 = BooleanField(q.option3)
		option4 = BooleanField(q.option4)
		submit = SubmitField("Cast Vote")
	return OptionForm()


class QuestionForm(FlaskForm):
	title = StringField("Enter the title")
	question = TextAreaField("Enter the question")
	option1 = StringField("Enter option 1")
	option2 = StringField("Enter option 2")
	option3 = StringField("Enter option 3")
	option4 = StringField("Enter option 4")
	submit = SubmitField("Make Question")
