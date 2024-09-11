from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse


# Create your views here.
def index(request): 
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    #params = {'no_of_slides':nSlides, 'range': range(nSlides),'product': products}
    allProds = [[products, range(1,len(nSlides)), nSlides],
                [products, range(1,len(nSlides)), nSlides],]
    
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("Shop Con")

def tracker(request):
    return HttpResponse("Shop tra")

def search(request):
    return HttpResponse("Shop sea")

def prodView(request):
    return HttpResponse("Shop prod view")

def checkOut(request):
    return HttpResponse("Shop check")