# verification/urls.py
from django.urls import path
from .views import verify_authenticity,homepage

app_name = 'verification'

urlpatterns = [
    path('verify-authenticity/', verify_authenticity, name='verify_authenticity'),
    path('homepage/', homepage, name='homepage'),
]
