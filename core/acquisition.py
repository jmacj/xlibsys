from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from core.forms import AcquisitionForm
from core.models import User, DoesNotExist, Acquisition, Inventory
from core.wrappers import authenticated, guest


app = Blueprint("acquisition", __name__)


@app.route('/add', methods=['POST'])
def add_acquisition():
	form = AcquisitionForm()
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
				tags=escape(form.tags.data),
				no_of_copies=escape(form.no_of_copies.data)
			)

			for x in range(0, int(form.no_of_copies.data)):
				Inventory.create(
					inventory_id=escape(form.bn.data) + escape('-') + escape(x),
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


@app.route('/update/<int:id>', methods=['POST'])
def update_acquisition(id):
	acq = Acquisition.get(Acquisition.bn == id)