import sys
import config

from flask import Flask, render_template, request, make_response, jsonify

# import crud;
import utils as cG;

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/verify", methods=['POST'])
def verify():
	req = request.json;
	# print(req['name'])
	if req != None or req != "":
		code = cG.generateCode()
		number = cG.numberFormatter(req['number'])

		if number is None:
			resp = jsonify(success=False, req=request.json, message="Number is not valid")
			resp.status_code = 404
			return resp

		user = add_user(req['name'], number, req['password'], code)

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

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
	"""docstring for User"""
	# id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	number = db.Column(db.Integer, unique=True, primary_key=True)
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
	number = db.Column(db.Integer)
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

    return user_schema.jsonify(new_user)

def verifiedUser(number):
	user = User.query.get(number)
	user.verified = True

	db.session.commit()

	return user_schema.jsonify(user)

def verifyCode(number, code):
	number = number;
	code = code;

	verification = Verification.query.get(number)
	data = VerificationSchema.jsonify(verification)

	if code == data.code:
		return true


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
		message = str(code) + " is your Africastalking verfication code"

		try:
			response = self.sms.send(message, recipients)
			print(response)
		except Exception as e:
			print('Encountered an error while sending: %s' % str(e))
			# raise e

		

### __ END AFRICASTALKING FUNCTIONS ###


if __name__ == '__main__':
	# env = sys.argv[1] if len(sys.argv) > 2 else 'dev'

	# if env == 'dev':
	# 	app.config = config.DevelopmentConfig
	# elif env == 'prod':
	# 	app.config = config.ProductionConfig
	# else:
	# 	raise ValueError('Invalid environment name')

	app.run(debug = True)