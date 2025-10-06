from django.urls import path, register_converter
from student.views import Home, Profile
from student.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', Home, name='Home'),
    # path('profile/1', Profile, name='Profile'), # static urls
    # path('profile/<my_id>', Profile, name='Profile'), # dynamic urls # if you don't konw str or int you can use this
    path('profile/<int:my_id>', Profile, name='Profile'),
    # path('profile/<slug:title>', Profile, name='Profile'),  # slug ex = http://127.0.0.1:8000/student/profile/master-django-in-01
    # path('profile/<str:title>', Profile, name='Profile'),
    # path('profile/<int:my_class>/<int:my_id>', Profile, name='Profile'),
    # path('profile/<yyyy:year>', Profile, name='Profile'), # custom path converter urls in Django
]