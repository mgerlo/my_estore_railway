from django.shortcuts import render
from .models import Product
# from django.http import HttpResponse
# Create your views here.


def commerce_home(request):
    products = Product.objects.all()
    return render(request, 'commerce/homepage.html', {'products': products})

def commerce_contattaci(request):
    return render(request, 'commerce/contattaci.html')

def commerce_carrello(request):
    return render(request, 'commerce/carrello.html')
