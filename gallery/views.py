from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location
# Create your views here.
def main(request):
    images=Image.objects.all()
    locations=Location.get_locations()
    print(locations)
    return render(request,'galleries/main.html',{'images:':images[::-1],'locations':locations})

def location(request, location):
    images= Image.filter_by_location(location)
    print(images)
    return render(request,'galleries/location.html',{'location_images':images})

def search(request):
    if 'searchedimage' in request.GET and request.GET['searchedimage']:
        category=request.GET.get('searchedimage')
        searched_images=Image.search_by_category(category)
        message=f'{category}'
        print(searched_images)
        return render(request, 'galleries/search.html',{'message':message,'images':searched_images})
    
    else:
        message='You have not searched for any image category'
        return render(request,'galleries/search.html',{'message':message})