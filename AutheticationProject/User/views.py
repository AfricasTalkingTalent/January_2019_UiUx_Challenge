from django.shortcuts import render
from .models import User
from rest_framework.decorators import (
    api_view, parser_classes, permission_classes)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
import uuid
from .models import User
import africastalking
from random import randint
from django.http import HttpResponse
from django.shortcuts import render


@api_view(['GET'])
@permission_classes((AllowAny, ))
@parser_classes((MultiPartParser, FormParser))
def get_users(request):
    """Returns details for all users in a JSOn format"""
    users = User.objects.all()
    context = {}
    for user in users:
        context = {
            str(user.id):
            {
                "first_name": user.first_name,
                "phone_number": user.phone_number,
                "last_name": user.last_name
            }
        }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def process_signup_data(request):
    """Accepts login data from a new user and creates the user in the db after verification"""
    data = request.data
    first_name = data["first_name"]
    last_name = data["last_name"]
    phone_number = data["phone_number"]
    email = data["email"]
    password = data["password"]
    user, created = User.objects.update_or_create(
        email_address=email,
        defaults={
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "password": password
        }
    )
    user.verification = generate_verification_code()
    user.save()
    send_sms_verification(user.phone_number, user.verification)
    return Response(status=status.HTTP_201_CREATED)


def send_sms_verification(phone_number: str, verification_code: str)->None:
    """sends an sms to the user to verify phone number"""
    username = "healthixAndroid"
    api_key = "04c322dfb5bf4b3b00414d55eb56f640389b8cb9e10226e9567c81bc086d5362"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send(
        "Hello, please send the code to complete your signup {}".format(verification_code), [phone_number])
    print(response)


def generate_verification_code()->str:
    """Returns a four digit verification code"""
    verification_code = randint(10**3, ((10**4) - 1))
    return str(verification_code)


@api_view(['POST'])
def process_verification(request):
    """Verifies the code sent to a user"""
    data = request.data
    email = data["email"]
    code = data["cod"]
    user = None
    try:
        user = User.objects.get(email_address=email)
    except:
        print("User not found")
        return Response(status=status.HTTP_404_NOT_FOUND)
    if user.verificaton == code:
        user.active = "True"
        user.verification = ""
        user.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_404_NOT_FOUND)


def load_login_page(request):
    return render(request, 'signup.html')


def verify_user(request):
    return render(request, 'verify.html')
