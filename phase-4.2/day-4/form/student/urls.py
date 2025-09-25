from django.urls import path
from student.views import registration, login, demo_form

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login, name='login'),
    path('demo/', demo_form, name='demo_form'),
]
