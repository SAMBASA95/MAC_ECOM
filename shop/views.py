from math import ceil
from django.shortcuts import render
from .models import Product
from .models import Contact
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
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact_info = Contact(name=name, email=email, phone=phone, desc=desc)
        contact_info.save()
        thank = True
        print(contact_info)
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("We Are In def search")


def products_view(request, my_id):
    # fetch the product using id
    product = Product.objects.filter(id=my_id)
    print(product, my_id)
    return render(request, 'shop/productView.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("We Are In def checkout")
