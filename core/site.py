from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from core.forms import AcquisitionForm, ReservationForm
from core.models import User, DoesNotExist, Acquisition, Inventory
from core.wrappers import authenticated, guest

app = Blueprint("site", __name__)

@app.route('/', methods=["GET"])
@authenticated
def index():
	# return jsonify(session['user'])
	book_count = Inventory.select().count()
	borrowed_count = Inventory.select().where(Inventory.status=='Borrowed').count()
	user_count = User.select().count()
	return render_template('nav/index.html', book_count=book_count, borrowed_count=borrowed_count, user_count=user_count)

@app.route('acquisition', methods=["GET"])
@authenticated
def acquisition():
	form = AcquisitionForm()
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/acquisition.html', form=form, success_message=success_message, error_message=error_message)

@app.route('circulation', methods=["GET"])
@authenticated
def circulation():
	# return jsonify(session['user'])
	return render_template('nav/circulation.html')

@app.route('inventory', methods=["GET"])
@authenticated
def inventory():
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/inventory.html', success_message=success_message, error_message=error_message)

@app.route('reservation', methods=["GET"])
@authenticated
def reservation():
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/reservation.html', success_message=success_message, error_message=error_message)

@app.route('opac/guest', methods=["GET"])
@guest
def opac_g():
	form = ReservationForm()
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/opac_g.html', form=form, success_message=success_message, error_message=error_message)


@app.route('opac', methods=["GET"])
@authenticated
def opac():
	form = ReservationForm()
	success_message = error_message = None
	# return jsonify(session['user'])
	return render_template('nav/opac.html', form=form, success_message=success_message, error_message=error_message)