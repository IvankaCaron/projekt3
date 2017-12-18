# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Spot


class MapPageView(TemplateView):
    template_name = 'map.html'



def point_datasets(request):
    points = serialize('geojson', Spot.objects.all())
    return HttpResponse(points, content_type= 'json')