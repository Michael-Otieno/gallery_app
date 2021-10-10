from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location
# Create your views here.
def main(request):
    images=Image.objects.all()
    locations=Location.get_locations()
    print(locations)
    return render(request,'gallery/index.html',{'images:':images[::-1],'locations':locations})