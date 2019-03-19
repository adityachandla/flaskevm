from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField




def getForm(q):
	class OptionForm(FlaskForm):
		option1 = BooleanField(q.option1)
		option2 = BooleanField(q.option2)
		option3 = BooleanField(q.option3)
		option4 = BooleanField(q.option4)
		submit = SubmitField("Cast Vote")
	return OptionForm()	