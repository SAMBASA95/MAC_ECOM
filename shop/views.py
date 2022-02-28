from math import ceil
from django.shortcuts import render
from .models import Product

# Create your views here.
from django.http import HttpResponse


def index(request):
    all_prod_list = []
    cat_prods = Product.objects.values('category', 'id')
    all_categories = {item['category'] for item in cat_prods}
    for category in all_categories:
        prod = Product.objects.filter(category=category)
        n = len(prod)
        n_slides = n // 3 + ceil((n / 3) - (n // 3))
        all_prod_list.append([prod, range(1, n_slides), n_slides])
    params = {'allProds': all_prod_list}
    return render(request, 'shop/index.html', params)


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
