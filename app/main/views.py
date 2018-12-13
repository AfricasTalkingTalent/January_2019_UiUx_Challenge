from flask import render_template, request, redirect, url_for

from . import main


from ..request import send_sms


@main.route('/')
def index():

    message = 'This is a tryx'
    number = '+254712725144'

    responds = send_sms(message, number)
    print(responds)
    return render_template('index.html', responds=responds)
