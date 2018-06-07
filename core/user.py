from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from werkzeug.local import LocalProxy
from werkzeug.security import generate_password_hash, check_password_hash

from core.forms import UserRegistrationForm, UserLoginForm
from core.models import User, DoesNotExist
from core.wrappers import authenticated, guest

app = Blueprint("user", __name__)

@app.route("/disintegrate", methods=["GET"])
def disintegrate():
	User.drop_table()
	return redirect('/user/register')

@app.route("/login", methods=["GET", "POST"])
@guest
def login():
	form = UserLoginForm()
	error_message = None
	if form.validate_on_submit():
		if request.method == 'POST':
			try:
				user = User.get(User.email_address == request.form['email_address'])
				if not check_password_hash(user.password, request.form['password']):
					error_message = 'Invalid Credentials.'
				else:
					session['user'] = user.id
					session['name'] = user.first_name + ' ' + user.last_name
					return redirect(url_for('site.index'))
			except DoesNotExist:
				error_message = 'Invalid Credentials.'

	return render_template('user/login.html', form=form, error_message=error_message)

@app.route('/logout', methods=['GET', 'POST'])
@authenticated
def logout():
	session.pop('user', None)
	return redirect(url_for('site.index'))

@app.route("/register", methods=["GET", "POST"])
@guest
def register():
	form = UserRegistrationForm()
	if form.validate_on_submit():
		if request.method == 'POST':
			User.create(
				first_name=escape(form.first_name.data),
				last_name=escape(form.last_name.data),
				email_address=escape(form.email_address.data),
				password=generate_password_hash(form.password.data)
			)
		return redirect(url_for('user.login'))
	return render_template("user/register.html", form=form)
