from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import login, logout


urlpatterns = [
    #url(r'^$', views.home, name='account'),
    path('', views.home, name='account'),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('register/', views.register, name='register' ),
]