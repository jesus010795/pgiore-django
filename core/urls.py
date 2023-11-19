from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company/', views.company, name='company'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('media/', views.media, name='media'),
]
