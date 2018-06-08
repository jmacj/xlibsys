from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from core.forms import AddAcquisitionForm
from core.models import User, DoesNotExist, Acquisition
from core.wrappers import authenticated, guest

app = Blueprint("site", __name__)

@app.route('/', methods=["GET"])
@authenticated
def index():
	# return jsonify(session['user'])
	return render_template('nav/index.html')

@app.route('acquisition', methods=["GET"])
@authenticated
def acquisition():
	form = AddAcquisitionForm()
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/acquisition.html', form=form, success_message=success_message, error_message=error_message)

@app.route('acquisition', methods=['POST'])
def add_acquisition():
	form = AddAcquisitionForm()
	success_message = None
	error_message = None
	if form.validate_on_submit():
		if request.method == 'POST':
			Acquisition.create(
				bn=escape(form.bn.data),
				title=escape(form.title.data),
				author=escape(form.author.data),
				publisher=escape(form.publisher.data),
				published_on=escape(form.published_on.data),
				tags=escape(form.tags.data)
			)
			success_message = "Successfully added new book"
		return render_template("nav/acquisition.html", form=form, success_message=success_message, error_message=error_message)
		error_message = "Failed to add new book"
	return render_template("nav/acquisition.html", form=form, success_message=success_message, error_message=error_message)

@app.route('circulation', methods=["GET"])
@authenticated
def circulation():
	# return jsonify(session['user'])
	return render_template('nav/circulation.html')

@app.route('inventory', methods=["GET"])
@authenticated
def inventory():
	# return jsonify(session['user'])
	return render_template('nav/inventory.html')

@app.route('reservation', methods=["GET"])
@authenticated
def reservation():
	# return jsonify(session['user'])
	return render_template('nav/reservation.html')

