from flask import Blueprint, jsonify

from markupsafe import escape

from core.forms import AddAcquisitionForm
from core.models import Acquisition

from datetime import datetime, date, time

import json

app = Blueprint('api', __name__)

@app.route('/acquisition', methods=['GET'])
def get_acquisition():
	return jsonify([row for row in Acquisition.select(Acquisition).dicts()])

@app.route('/acquisition/dis', methods=['GET'])
def del_acquisition():
	Acquisition.drop_table()
	return jsonify([row for row in Acquisition.select(Acquisition).dicts()])


