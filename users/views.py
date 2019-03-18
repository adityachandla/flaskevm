from users import user
from flask import render_template, redirect, flash, session
from users.models import UserModel
from users.forms import SignIn,SignUp



@user.route("/")
def signin():
	if 'username' in session:
		del session["username"]
	form = SignIn()
	if form.validate_on_submit():
		possible_usrs = UserModel.query.filter_by(username=form.username.data).first()
		if possible_usrs == None:
			flash("Username not found")
			return redirect("/")
		if possible_usrs.password == form.password.data:
			session["username"] = form.username.data
			return redirect("/home")
		flash("Invalid Password")
		return redirect("/")
	return render_template("signup.html",form = form)


@user.route("/signup")
def signup():
	if 'username' in session:
		del session["username"]
	form = SignUp()
	if form.validate_on_submit():
		already_taken = UserModel.query.filter_by(username=form.username.data).first()
		if already_taken != None:
			flash("Username already taken")
			return redirect("/signup")
		if form.password.data != form.password2.data:
			flash("Passwords don't match")
			return redirect("/signup")
		new_user = UserModel(username=form.username.data,password=form.password.data,email=form.email.data)
		db.session.add(new_user)
		db.session.commit()
	return render_template("singup.html",form=form)