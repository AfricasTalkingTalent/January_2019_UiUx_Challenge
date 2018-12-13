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
    user, created = User.objects.update_or_create(
        email_address=email,
        defaults={
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
        }
    )
    send_sms_verification(user.phone_number)
    return Response(status=status.HTTP_201_CREATED)


def send_sms_verification(phone_number: str)->None:
    """sends an sms to the user to verify phone number"""
    username = "healthixAndroid"
    apikey = "04c322dfb5bf4b3b00414d55eb56f640389b8cb9e10226e9567c81bc086d5362"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    verification_code = generate_verification_code()
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
        user.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_404_NOT_FOUND)
