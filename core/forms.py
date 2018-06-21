from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, DateTimeField, SelectField, DecimalField, IntegerField
from wtforms.fields import DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, ValidationError, Optional, Email, EqualTo

from core.models import User, Inventory


from datetime import datetime

class UserRegistrationForm(FlaskForm):
	first_name = StringField('First Name', [Required()])
	last_name = StringField('Last Name', [Required()])
	email_address = EmailField('Email', [Required(), Email()])
	password = PasswordField('Password', [Required(), EqualTo('confirm_password', message='Password must match')])
	confirm_password = PasswordField('Retype password', [Required()])

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email is already in use.')

class UserLoginForm(FlaskForm):
    email_address = EmailField('Email Address', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class AcquisitionForm(FlaskForm):
	bn = StringField('Book ID', [Required()])
	title = StringField('Title', [Required()])
	author = StringField('Author', [Required()])
	publisher = StringField('Publisher')
	published_on = DateField('Date Published')
	tags = StringField('Category')
	no_of_copies = IntegerField('No of copies', [Required()])

class ReservationForm(FlaskForm):
	inventory_id = StringField('Book ID', [Required()])
