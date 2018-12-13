from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from User.views import get_users, process_signup_data, process_verification,load_login_page,verify_user
admin.site.site_header = "Brian Verification Application"
admin.site.site_title = "Brian Admin Verification"
admin.site.index_title = "Welcome to Brian Vefification Application"
router = DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-users', get_users),
    path('sign-up', process_signup_data),
    path('verify', process_verification),
    path('home',load_login_page),
    path('verify-user',verify_user)
]
