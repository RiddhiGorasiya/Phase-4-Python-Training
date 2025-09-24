from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Home Page')

# def learn_django(request):
#     return HttpResponse('Hello Django')

# def learn_python(request):
#     return HttpResponse('<h1>Hello python<h1/>')

# def learn_math(request):
#     a = 10 + 10
#     return HttpResponse(a)

# def learn_php(request):
#     lang = '<h1>Hello PHP<h1/>'
#     return HttpResponse(lang)

# URL Configuration with additional parameters
def learn_django(request, **kwargs):
    status = kwargs.get('status', 'inactive')
    return HttpResponse(f'<h1>Hello Django {status} - App1<h1/>')
