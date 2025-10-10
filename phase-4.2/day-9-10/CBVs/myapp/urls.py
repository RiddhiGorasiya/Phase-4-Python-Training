from django.urls import path 
from myapp import views
urlpatterns = [
    # path('fun1/', views.myfunview1, name='myfunview1'),
    # path('fun2/', views.myfunview2, name='myfunview2'),
    # path('homefun/', views.homefunview, name='homefunview'),
    # path('aboutfun/', views.aboutfunview, name='aboutfunview'),
    # path('newsfun/', views.newsfunview, name='newsfunview'),
    # # path('newsfun2/', views.newsfunview, {'template_name':'myapp/news2.html'}, name='news_fun2_view'),
    # path('contactfun/', views.contactfunview, name='contactfunview'),

    path('cl1/', views.MyClassView1.as_view(), name='MyClassView1'),
    path('cl2/', views.MyClassView2.as_view(), name='MyClassView2'),
    path('cl3/', views.MyClassView3.as_view(), name='MyClassView3'),
    path('home/', views.HomeClassView.as_view(), name='HomeClassView'),
    path('about/', views.AboutClassView.as_view(), name='AboutClassView'),
    path('news/', views.NewsClassView.as_view(template_name = 'myapp/news.html'), name='NewsClassView'),
    path('news2/', views.NewsClassView.as_view(template_name = 'myapp/news2.html'), name='NewsClassView'),
    # path('contact/', views.ContactClassView.as_view(), name='ContactClassView'),
]
