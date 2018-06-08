from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, DateTimeField, SelectField, DecimalField, IntegerField
from wtforms.fields import DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, ValidationError, Optional, Email, EqualTo


from datetime import datetime

class UserRegistrationForm(FlaskForm):
	first_name = StringField('First Name', [Required()])
	last_name = StringField('Last Name', [Required()])
	email_address = EmailField('Email', [Required()])
	password = PasswordField('Password', [Required(), EqualTo('confirm_password', message='Password must match')])
	confirm_password = PasswordField('Retype password', [Required()])

class UserLoginForm(FlaskForm):
    email_address = EmailField('Email Address', [Required()])
    password = PasswordField('Password', [Required()])

class AddAcquisitionForm(FlaskForm):
	bn = StringField('Book ID', [Required()])
	title = StringField('Title', [Required()])
	author = StringField('Author', [Required()])
	publisher = StringField('Publisher')
	published_on = DateField('Date Published')
	tags = StringField('Category')
# class CreateEmployeeForm(FlaskForm):
# 	email_address = StringField('Email Address', [Required(), Email()])
	
# 	first_name = StringField('First Name', [Required()])
# 	last_name = StringField('Last Name', [Required()])
# 	middle_name = StringField('Middle Name', [Required()])
# 	gender = SelectField('Gender', [Required()], choices=[('1', 'Male'), ('2', 'Female')])
# 	address = StringField('Address', [Required()])
# 	contact_number = StringField('Contact Number', [Required()])
# 	birth_date = DateTimeField('Birth Date', [Required()], format='%Y-%m-%d')
	
# 	position_id = SelectField('Position', [Required()], coerce=int)
# 	schedule_id = SelectField('Schedule', [Required()], coerce=int)
# 	department_id = SelectField('Department', [Required()], coerce=int)
# 	employment_date = DateTimeField('Employment Date', [Required()], format='%Y-%m-%d')
# 	salary = DecimalField('Salary', [Required()], places=2)
	
# 	sss = StringField('SSS', [Optional()])
# 	pagibig = StringField('Pag-ibig', [Optional()])
# 	philhealth = StringField('PhiHealth', [Optional()])
# 	tin = StringField('TIN', [Optional()])
	
# 	vacation_leaves = IntegerField('Vacation Leaves', [Required()], default=0)
# 	sick_leaves = IntegerField('Sick Leaves', [Required()], default=0)
