from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Gallery
def product(request):
    all_product = Product.objects.all()
    all_image = Gallery.objects.all()
    return render(request, 'products/product.html', {'all_product': all_product, 'all_image': all_image})

def product_id(request, product_id):
    try:
        a = Product.objects.get(id = product_id)
    except:
        raise Http404("Страница не найдена!")
    return render(request, 'products/product.html', {'products': a})
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about/about.html')