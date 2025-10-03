from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            cpw = form.cleaned_data['confirm_password']
            # print('Name:', nm)
            # print('Email:', em)
            # print('Password:', pw)
            # print('Confirm_Password', cpw) # this data show in terminal
            # Syntax:- save(commit=False/True)
            # save data into database
            pr = Profile(name=nm, email=em, password=pw) 
            pr.save()
            # update data into database
            pr = Profile(id = 2, name=nm, email=em, password=pw) 
            pr.save()
            # delete data into database
            pr = Profile(id = 2) 
            pr.delete()
            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form': form})