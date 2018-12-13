from django import forms
from models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','lasxt_name','email_address','phone_number','active','password')