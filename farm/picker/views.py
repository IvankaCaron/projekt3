# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Spot
from django import forms
from leaflet.forms.widgets import LeafletWidget


class MapPageView(TemplateView):
    template_name = 'map.html'


def point_datasets(request):
    points = serialize('geojson', Spot.objects.all())
    return HttpResponse(points, content_type= 'json')


class SpotForm(forms.ModelForm):


    class Meta:
        model = Spot
        fields = ('name', 'user', 'typeProduct', 'location', 'description')
        widgets = {'location': LeafletWidget()}



class EditSpot(UpdateView):
    model = Spot
    form_class = SpotForm
    template_name = 'form.html'

def insertData(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SpotForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return redirect('/map')
    else:
        form = SpotForm() # An unbound form
        return render(request, 'form.html',{'form': form})
