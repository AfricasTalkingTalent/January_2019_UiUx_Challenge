from flask import render_template, request, redirect, url_for
from ..models import User
from .forms import RegistrationForm
from .. import db
from random import choices

from . import main


from ..request import send_sms


@main.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():

    return render_template('register.html', reg_form=form)


@main.route('/')
def index():

    message = 'This is a tryx'
    number = '+254712725144'

    responds = send_sms(message, number)
    print(responds)
    return render_template('index.html', responds=responds)
