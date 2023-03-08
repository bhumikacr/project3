from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('Bhumi/',Bhumi,name='Bhumi'),
    path('keerthi/',keerthi,name='keerthi'),
]