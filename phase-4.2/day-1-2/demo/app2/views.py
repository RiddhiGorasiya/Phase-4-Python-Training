from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myApp2(request):
    return HttpResponse(f'<h1>Hello mtApp2<h1/>')