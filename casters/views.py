from flask import render_template, redirect, session, flash
from casters import caster,db
from casters.models import VoteModel, QuestionModel
from casters.forms import getForm, QuestionForm

@caster.route("/home")
def home():
	if 'username' not in session:
		return redirect("/")
	questions = QuestionModel.query.all()
	return render_template("home.html",questions=questions)



@caster.route("/home/<title>",methods=["GET","POST"])
def poll(title):
	if 'username' not in session:
		return redirect("/")
	## checking if the user has already cast his vote
	q = QuestionModel.query.filter_by(title=title).first()
	voted = VoteModel.query.filter_by(title=q.title).filter_by(username=session['username']).first()
	if voted != None:
		flash("You have already cast your vote")
		return redirect("/home/"+title+"/summary")

	form = getForm(q)
	if form.validate_on_submit():
		l = [form.option1.data,form.option2.data,form.option3.data,form.option4.data]
		if l.count(True) != 1:
			flash("Invalid Selection")
			return redirect('/home/'+title)
		option_selected = l.index(True)+1
		vote = VoteModel(username=session['username'],title=q.title,option=option_selected)
		db.session.add(vote)
		db.session.commit()
		return redirect("/home/"+title+"/summary")
	return render_template("question.html",form=form,question=q)



@caster.route("/home/<title>/summary")
def summary(title):
	all_votes = VoteModel.query.filter_by(title=title).all()
	options = [0]*4
	for i in all_votes:
		options[i.option-1] += 1
	q = QuestionModel.query.filter_by(title=title).first()
	return render_template("summary.html",question=q,options=options)


@caster.route("/newpoll", methods=["GET","POST"])
def newpoll():
	form = QuestionForm()
	if form.validate_on_submit():
		new_question = QuestionModel(title=form.title.data,question=form.question.data,
			option1=form.option1.data,option2=form.option2.data,option3=form.option3.data,option4=form.option4.data)
		db.session.add(new_question)
		db.session.commit()
		flash("Question added successfully")
		return redirect("/home")
	return render_template('new.html',form=form)


@caster.route("/logout")
def logout():
	if 'username' in session:
		del session['username']
	return redirect('/')
