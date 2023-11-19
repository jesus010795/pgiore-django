from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, template_name='core/home.html')


def company(request):
    return render(request, template_name='core/company.html')


def services(request):
    return render(request, template_name='core/services.html')


def products(request):
    return render(request, template_name='core/products.html')


def contact(request):
    return render(request, template_name='core/contact.html')


def media(request):
    return render(request, template_name='core/media.html')