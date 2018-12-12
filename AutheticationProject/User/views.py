from django.shortcuts import render
from .models import User
from rest_framework.decorators import (
    api_view, parser_classes, permission_classes)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser


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
