from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Bhoomi(request):
    return HttpResponse('MY LUCKY NUMBER IS 14')
def Nalini(request):
    return HttpResponse('<h1>MY MORTHER NAME IS NALINI</h1>')
