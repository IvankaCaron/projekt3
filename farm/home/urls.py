from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('connect/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friends, name ='change_friends'),
    path('connect/<operation>/<int:pk>/', views.change_friends, name ='change_friends'),
]
