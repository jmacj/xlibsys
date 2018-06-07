from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for, session
from markupsafe import escape

from core.forms import UserRegistrationForm, UserLoginForm
from core.models import User, DoesNotExist
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
	# return jsonify(session['user'])
	return render_template('nav/acquisition.html')

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

