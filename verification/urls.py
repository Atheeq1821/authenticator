# verification/urls.py
from django.urls import path
from .views import *

app_name = 'verification'

urlpatterns = [
    path('verify-authenticity/', verify_authenticity, name='verify_authenticity'),
    path('openAddKeys/', openAddKeys, name='openAddKeys'),
    path('appendKeys/', appendKeys, name='appendKeys'),
    path('replaceKeys/', replaceKeys, name='replaceKeys'),
    path('homepage/', homepage, name='homepage'),
    path('dianabol/', dianabol, name='dianabol'),
    path('anavar/', anavar, name='anavar'),
    path('clen/', clen, name='clen'),
    path('winr/', winr, name='winr'),
    path('anadrol/', anadrol, name='anadrol'),
    path('loadpro/', loadProduct, name='loadProduct'),
]
