from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    car_title_search = Car.objects.values_list('car_title', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()




    data = {
        'cars': paged_cars,
        'car_title_search': car_title_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
    }
    return render (request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk= id)

    data = {
        'single_car': single_car,
    }
    return render (request, 'cars/car_detail.html',data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    car_title_search = Car.objects.values_list('car_title', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transm_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            cars = cars.filter(description__icontains=keywords)

    if 'car_title' in request.GET:
        car_title = request.GET['car_title']
        
        if car_title:
            cars = cars.filter(car_title__iexact=car_title)

    if 'city' in request.GET:
        city = request.GET['city']
        
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
           cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars' : cars,
        'car_title_search': car_title_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
        'transm_search' : transm_search,
    }
    return render(request, 'cars/search.html', data)