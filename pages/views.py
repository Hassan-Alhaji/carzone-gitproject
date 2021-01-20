from cars.views import search
from django.shortcuts import render
from .models import team
from cars.models import Car

# Create your views here.

def home(request):
    teams = team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    car_title_search = Car.objects.values_list('car_title', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data =  {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'all_cars': all_cars,
        'car_title_search': car_title_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
    }
    return render (request, 'pages/home.html', data)

def about(request):
    teams = team.objects.all()
    data =  {
        'teams' : teams,
    }
    return render (request, 'pages/about.html', data)

def services(request):
    return render (request, 'pages/services.html')

def contact(request):
    return render (request, 'pages/contact.html')