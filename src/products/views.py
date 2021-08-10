from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Gallery
from django.shortcuts import get_object_or_404


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product': product})

def product(request):
    product_home = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_home.html', {'product_home': product_home})


def home(request):
    products_home = get_object_or_404(Product.objects.all())
    return render(request, 'home.html', {'products_home': products_home})


def about(request):
    return render(request, 'about/about.html')