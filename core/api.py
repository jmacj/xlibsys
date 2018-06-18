from flask import Blueprint, jsonify

from markupsafe import escape

from core.models import Acquisition, Inventory

from datetime import datetime, date, time

import json

app = Blueprint('api', __name__)

@app.route('/acquisition', methods=['GET'])
def get_acquisition():
	return jsonify([row for row in Acquisition.select(Acquisition).dicts()])

@app.route('/dis', methods=['GET'])
def del_acquisition():
	Acquisition.drop_table()
	Inventory.drop_table()
	return 'deleted'

@app.route('/inventory', methods=['GET'])
def get_inventory():
	return jsonify([row for row in Inventory.select(Inventory).dicts()])

