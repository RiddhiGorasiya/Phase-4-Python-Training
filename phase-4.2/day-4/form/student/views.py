from django.shortcuts import render
from student.forms import Registration, Login, DemoForm
# Create your views here.

def registration(request):
    fm = Registration()
    return render(request, 'student/registration.html', {'form' : fm})

def login(request):
    fm = Login(auto_id=True)
    return render(request, 'student/login.html', {'form' : fm})

def demo_form(request):
    form = DemoForm()
    return render(request, 'student/demoform.html', {'form': form})