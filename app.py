import sys
import config
import json

from flask import Flask, render_template, request, make_response, jsonify

import utils;

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/", methods=['GET', 'POST'])
def index():
	error = None
	user = None

	if request.method == 'POST':
		req = request.form
		num = utils.numberFormatter(req['number'])

		verification = verifyCode(num, req['code'])

		if verification:
			verified = verifiedUser(num)

			return render_template('success.html', user = verified)
		else:
			deleteVerification(num)
			error = 'Invalid credentials'
			user = {
				'name': req['name'],
				'number': num,
				}

	return render_template('index.html', error = error, user = user)


@app.route("/sendOTP", methods=['POST'])
def sendOTP():
	req = request.json;

	if req != None or req != "":
		code = utils.generateCode()
		number = utils.numberFormatter(req['number'])

		if number is None:
			resp = jsonify(success=False, req=request.json, message="Number is not valid")
			resp.status_code = 404
			return resp

		checkForUserAndAdd(req['name'], number, req['password'], code)

		SMS().send_sms_sync(number, code)

		resp = jsonify(success=True, req=req)
		resp.status_code = 200
	else:
		resp = jsonify(success=False, req=request.json, message="request cannot be null")
		resp.status_code = 404
		
	return resp


### CRUD FUNCTIONS ###

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import datetime

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
	"""docstring for User"""
	name = db.Column(db.String(32))
	number = db.Column(db.String(15), primary_key=True)
	password = db.Column(db.String(190))
	verified = db.Column(db.Boolean, default=False)

	def __init__(self, name, number, password):
		super(User, self).__init__()
		self.name = name
		self.number = number
		self.password = password
		
class UserSchema(ma.Schema):
	"""docstring for UserSchema"""
	class Meta:
		# Fields to expose
		fields = ('name', 'number', 'password', 'verified')
		
user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Verification(db.Model):
	"""docstring for Verification"""
	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.String(15))
	code = db.Column(db.Integer)
	expiryDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(self, number, code):
		super(Verification, self).__init__()
		self.number = number
		self.code = code
		
class VerificationSchema(ma.Schema):
	"""docstring for VerificationSchema"""
	class Meta:
		fields = ('number', 'code', 'expiryDate')

verification_schema = VerificationSchema()
verifications_schema = VerificationSchema(many=True)

def add_user(name, number, password, code):
    name = name;
    number = number;
    password = password;

    new_user = User(name, number, password)

    db.session.add(new_user)
    db.session.commit()

    new_verification = Verification(number, code)

    db.session.add(new_verification)
    db.session.commit()

    return new_user

def checkForUserAndAdd(name, number, password, code):
	user = User.query.filter_by(number=number).first()

	if user is None:
		user = add_user(name, number, password, code)
	else:
		user.name = name
		user.number = number
		user.password = password
		db.session.commit()

		new_verification = Verification(number, code)

		db.session.add(new_verification)
		db.session.commit()

	return user_schema.jsonify(user)


def verifiedUser(number):
	user = User.query.filter_by(number=number).first()
	user.verified = True

	db.session.commit()

	return json.loads(user_schema.dumps(user).data)

def verifyCode(number, code):
	number = number;
	code = code;

	verification = Verification.query.filter_by(number=number).order_by('-id')[0]

	data = json.loads(verification_schema.dumps(verification).data)

	if int(code) == data['code']:
		db.session.delete(verification)
		db.session.commit()
		return True

	return False

def deleteVerification(number):
	verification = Verification.query.filter_by(number=number).first()

	db.session.delete(verification)
	db.session.commit()

	return True


### __ END CRUD FUNCTIONS ###



### AFRICASTALKING FUNCTIONS ###

# from __future__ import print_function
import africastalking

class SMS:
	"""docstring for SMS"""
	def __init__(self):
		self.username = app.config['AS_USERNAME']
		self.api_key = app.config['AS_API_KEY']

		africastalking.initialize(self.username, self.api_key)

		self.sms = africastalking.SMS

	def send_sms_sync(self, number, code):
		recipients = [number]
		message = str(code) + " is your Africastalking verification code"

		try:
			response = self.sms.send(message, recipients)
			print(response)
		except Exception as e:
			print('Encountered an error while sending: %s' % str(e))
			# raise e

### __ END AFRICASTALKING FUNCTIONS ###


if __name__ == '__main__':
	app.run()