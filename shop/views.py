from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("We Are In def about")


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