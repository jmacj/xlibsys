from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from core.forms import AcquisitionForm, ReservationForm
from core.models import User, DoesNotExist, Acquisition, Inventory, Reservation
from core.wrappers import authenticated, guest

import datetime

app = Blueprint("reservation", __name__)


@app.route('/add', methods=['POST'])
def add_reservation():
	form = ReservationForm()
	success_message = error_message = None
	if form.validate_on_submit():
		if request.method == 'POST':
			book = Inventory.get_or_none(Inventory.inventory_id==form.inventory_id.data)
			if book == None:
				error_message='Book not found.'
			else:
				if book.status != 'On Shelf':
					error_message='Book not available'
				else:
					Reservation.create(
						book_id=book.inventory_id,
						user=session['user'],
						reservation_date=datetime.datetime.now()
					)
					success_message = "Reservation Success"
		return render_template("nav/opac.html", form=form, success_message=success_message, error_message=error_message)
		error_message = "Reservation Failed"
	return render_template("nav/opac.html", form=form, success_message=success_message, error_message=error_message)

@app.route('/update', methods=['GET'])
@app.route('/update/<res_id>', methods=['GET'])
def update_reservation(res_id):
	success_message = error_message = None
	reservation = Reservation.get(Reservation.id==res_id)
	book = Inventory.get(Inventory.inventory_id==reservation.book_id)
	if book.status == 'Out':
		error_message='Book is already reserved.'
	elif reservation.status == 'Pending':
		reservation.update(status='Reserved', due_date=datetime.datetime.now() + datetime.timedelta(days=5)).where(Reservation.id==reservation.id).execute()
		book.update(status='Out').where(Inventory.inventory_id==reservation.book_id).execute()
		success_message='Book successfully reserved.'
	else:
		error_message='Book is already returned'

	return render_template("nav/reservation.html", success_message=success_message, error_message=error_message)


@app.route('/add/<res_id>', methods=['GET'])
def reserve(res_id):
	form = ReservationForm()
	success_message = None
	error_message = None
	book = Inventory.get_or_none(Inventory.inventory_id==res_id)

	if book.status != 'On Shelf':
		error_message='Book not available'
	else:
		Reservation.create(
			book_id=book.inventory_id,
			user=session['user'],
			reservation_date=datetime.datetime.now()
		)
		success_message = "Reservation Success"
	return render_template("nav/opac.html", form=form, success_message=success_message, error_message=error_message)