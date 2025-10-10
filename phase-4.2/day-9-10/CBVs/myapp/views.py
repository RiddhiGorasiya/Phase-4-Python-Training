from django.shortcuts import render, HttpResponse
from myapp.forms import ContactForm
from django.views import View

# Create your views here.

# def myfunview1(request):
#     return HttpResponse("Hello Function Based view")
class MyClassView1(View):
    def get(self, request):
        return HttpResponse("Hello Class Based view")

# def myfunview2(request):
#     return HttpResponse("<h1>Hello Function Based view</h1>")
class MyClassView2(View):
    def get(self, request):
        return HttpResponse("<h1>Hello Class Based view</h1>")

class MyClassView3(View):
    name = "Riddhi"
    def get(self, request):
        return HttpResponse(self.name)

# def homefunview(request):
#     return render(request, 'myapp/home.html')
class HomeClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')

# def aboutfunview(request):
#     context = {'msg' : 'Welcome to Function Base View'}
#     return render(request, 'myapp/about.html', context)
class AboutClassView(View):
    def get(self, request):
        context = {'msg' : 'Welcome to Class Base View'}
        return render(request, 'myapp/about.html', context)

# def newsfunview(request, template_name):
#     template_name = template_name
#     context = {'info' : 'Subscribe to news channel'}
#     return render(request, template_name, context)
class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info' : 'Subscribe to news channel'}
        return render(request, self.template_name, context)

# def contactfunview(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#         return HttpResponse('Thank You Form Submitted !!')
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form':form})
# class ContactClassView(View):
#     def get(Self, request):
#         form = ContactForm()
#         return render(request, 'myapp/contact.html', {'form':form})
#     def post ContactForm(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#         return HttpResponse('Thank You Form Submitted !!')
