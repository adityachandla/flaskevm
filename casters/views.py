from flask import render_template, redirect, session
from casters import caster
from casters.models import VoteModel, QuestionModel
from casters.forms import getForm

@caster.route("/home")
def home():
	if 'username' not in session:
		return redirect("/")
	questions = QuestionModel.query.all()
	return render_template("home.html",questions=questions)



@caster.route("/home/<title>",methods=["GET","POST"])
def poll(title):
	q = QuestionModel.query.filter_by(title=title).first()
	form = getForm(q)
	if form.validate_on_submit():
		print("you are a fucking genius")
		return redirect("/home/"+title+"/summary")
	return render_template("question.html",form=form,question=q)



@caster.route("/home/<title>/summary")
def summary(title):
	pass
