from flask import Blueprint, jsonify

from markupsafe import escape

from core.models import Acquisition, Inventory, Reservation, User

from datetime import datetime, date, time

import json

app = Blueprint('api', __name__)

@app.route('/acquisition', methods=['GET'])
def get_acquisition():
	return jsonify([row for row in Acquisition.select(Acquisition).dicts()])

@app.route('/dis', methods=['GET'])
def del_acquisition():
	Reservation.drop_table()
	Acquisition.drop_table()
	Inventory.drop_table()
	return 'deleted'

@app.route('/inventory', methods=['GET'])
def get_inventory():
	return jsonify([row for row in Inventory.select(Inventory).dicts()])

@app.route('/reservation', methods=['GET'])
def get_reservation():
	return jsonify([row for row in User.select(Reservation, Inventory.title, User.email_address).join(Reservation).join(Inventory).dicts()])