from math import ceil
from django.shortcuts import render
from .models import Product

# Create your views here.
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    n = len(products)
    nu_slides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nu_slides, 'range': range(1, 2), 'product': products}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We Are In def contact")


def tracker(request):
    return HttpResponse("We Are In def tracker")


def search(request):
    return HttpResponse("We Are In def search")


def product_view(request):
    return HttpResponse("We Are In def product_view")


def checkout(request):
    return HttpResponse("We Are In def checkout")
