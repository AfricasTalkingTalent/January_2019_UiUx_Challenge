from flask import render_template, request, redirect, url_for, session, Response
from ..models import User
from .forms import RegistrationForm, TokenForm
from .. import db
import random
import string

from . import main


from ..request import send_sms


def generate_token():
    '''
    generate random alphanumeric token upto 9 chars
    '''
    token = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for i in range(9))
    return token


def send_token(name, phone_number, token):
    '''
    sends token to phone
    '''
    message = f"Thank {name} please confirm account with {token}."

    responds = send_sms(message, phone_number)
    print(responds)
    return responds


@main.route('/', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        phone_number = form.phone_no.data
        username = form.username.data
        password = form.password.data

        token = generate_token()
        send_token(username, phone_number, token)

        session['phone_number'] = phone_number
        session['username'] = username
        session['password'] = password
        session['token'] = token
        print(phone_number)
        return redirect(url_for("main.token"))
    return render_template('register.html', reg_form=form)


@main.route('/token', methods=["GET", 'POST'])
def token():
    tform = TokenForm()
    if tform.validate_on_submit():
        token = tform.token.data
        phone_number = session.get('phone_number')
        username = session.get('username')
        password = session.get('password')
        token_ori = session.get('token')
        if token == token_ori:
            # user = User(phone_no=phone_number,
            #             username=username, password=password)
            # db.session.add(user)
            # db.session.commit()
            return Response("<h1>Success!</h1>")
    return render_template('token.html', tform=tform)


# @main.route('/')
# def index():

#     return render_template('index.html')
