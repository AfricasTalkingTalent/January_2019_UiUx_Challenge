from flask import render_template

from app import app

from .request import send_sms


@app.route('/')
def index():

    message = 'This is a tryx'
    number = '+254712725144'

    responds = send_sms(message, number)
    print(responds)
    return render_template('index.html', responds=responds)
