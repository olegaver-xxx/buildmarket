from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Gallery
from django.shortcuts import get_object_or_404


# def product(request):
#     all_product = Product.objects.all()
#     all_image = Gallery.objects.all()
#     return render(request, 'products/product.html', {'all_product': all_product, 'all_image': all_image})


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={'products': products})


def about(request):
    return render(request, 'about/about.html')