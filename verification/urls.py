# verification/urls.py
from django.urls import path
from .views import *

app_name = 'verification'

urlpatterns = [
    path('verify-authenticity/', verify_authenticity, name='verify_authenticity'),
    path('homepage/', homepage, name='homepage'),
    path('dianabol/', dianabol, name='dianabol'),
    path('anavar/', anavar, name='anavar'),
    path('clen/', clen, name='clen'),
    path('winr/', winr, name='winr'),
    path('anadrol/', anadrol, name='anadrol'),
    path('deca/', deca, name='deca'),
    path('bold/', bold, name='bold'),
    path('winstrol/', winstrol, name='winstrol'),
    path('mast/', mast, name='mast'),
    path('prime/', prime, name='prime'),
    path('susta/', susta, name='susta'),
    path('trena/', trena, name='trena'),
    path('tcyp/', tcyp, name='tcyp'),
    path('tpro/', tpro, name='tpro'),
]
