from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.

# home view
def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts':posts})

# about view
def about(request):
    return render(request, 'blogapp/about.html')

# contact view
def contact(request):
    return render(request, 'blogapp/contact.html')

# dashboard view
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blogapp/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
    
# logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# signup view
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an Author.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blogapp/signup.html', {'form':form})

# login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                messages.success(request, 'Logged in Successfully !!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blogapp/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                form = PostForm()
            messages.success(request, 'Post added successfully !!')
            return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm()
        return render(request, 'blogapp/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        messages.success(request, 'Post updated successfully !!')
        return render(request, 'blogapp/updatepost.html', {'form':form})         
    else:
        return HttpResponseRedirect('/login/')

# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Post deleted successfully !!')
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')