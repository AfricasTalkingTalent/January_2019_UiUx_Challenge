from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from User.views import get_users, process_signup_data
router = DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-users', get_users),
    path('login', process_signup_data),
]
