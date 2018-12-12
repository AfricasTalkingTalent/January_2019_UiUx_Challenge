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
    return Response(status=status.HTTP_201_CREATED)
