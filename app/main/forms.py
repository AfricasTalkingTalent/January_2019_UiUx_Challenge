from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('Enter your username', validators=[Required()])
    phone_no = StringField('Your phone number start with country code eg +XXX phone number',
                           validators=[Required()])
    # password = PasswordField('Password', validators=[Required(), EqualTo(
    #     'password_confirm', message='Passwords must match')])
    # password_confirm = PasswordField(
    #     'Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    # def validate_email(self, data_field):
    #     if User.query.filter_by(phone_no=data_field.data).first():
    #         raise ValidationError('There is an account with that phone number')

    # def validate_username(self, data_field):
    #     if User.query.filter_by(username=data_field.data).first():
    #         raise ValidationError('That username is taken')


class TokenForm(FlaskForm):
    token = StringField('Please enter security token?',
                        validators=[Required()])
    submit = SubmitField('token')
