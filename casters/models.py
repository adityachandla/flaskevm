from casters import db


class QuestionModel(db.Model):
	index = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String,unique=True)
	question = db.Column(db.String)
	option1 = db.Column(db.String)
	option2 = db.Column(db.String)
	option3 = db.Column(db.String)
	option4 = db.Column(db.String)


class VoteModel(db.Model):
	index = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String)
	title = db.Column(db.String)
	option = db.Column(db.Integer)