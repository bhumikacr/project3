from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('Bhoomi/',Bhoomi,name='Bhoomi'),
    path('Nalini/',Nalini,name='Nalini'),
]