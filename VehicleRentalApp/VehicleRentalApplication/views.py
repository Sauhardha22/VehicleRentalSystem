from django.shortcuts import render
from .models import Vehicle
from .models import VehicleMap
# Create your views here.
def home(request):
    vehicles = Vehicle.objects.all()
    return render(request,'home.html',{'vehicles':vehicles})

def map_view(request):
    vehicles = Vehicle.objects.all()
    return render(request,'rental/map.html',{'vehicles':vehicles})
# Create your views here.
