from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Bhumi(request):
    return HttpResponse('<h3>MY NAME IS <i>BHUMIKA</i></h3>')
def keerthi(request):
    return HttpResponse('<h1>MY NAME IS KEERTHANA</h1>')
