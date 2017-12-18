from django.conf.urls import include, url

from .views import MapPageView, point_datasets

urlpatterns = [
    url(r'^$', MapPageView.as_view(), name= 'myMap'),
    url(r'^spot_data/$', point_datasets, name='spot'),
    ]