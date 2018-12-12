import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email_address = models.CharField(max_length=250,blank=True,null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
