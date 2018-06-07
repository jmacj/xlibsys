from flask import Blueprint, jsonify

from core.models import Acquisition

from datetime import datetime, date, time

import json

app = Blueprint('api', __name__)

@app.route('/acquisition', methods=['GET'])
def get_acquisition():
	return jsonify([row for row in Acquisition.select(Acquisition).dicts()])
