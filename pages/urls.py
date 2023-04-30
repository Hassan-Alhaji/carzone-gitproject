from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='About'),
    path('cars',views.cars,name='Cars'),
    path('services',views.services,name='Services'),
    path('contact',views.contact,name='Contacts'),
]