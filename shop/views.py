from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'shop/index.html')

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