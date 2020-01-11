from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
    # return HttpResponse("<h1>Index Shop</h1>")

def about(request):
    return HttpResponse("<h1>About EKommerce</h1>")

def contact(request):
    return HttpResponse("<h1>Contact eKommerce</h1>")

def tracker(request):
    return HttpResponse("<h1>Tracker eKommerce</h1>")

def search(request):
    return HttpResponse("<h1>Search eKommerce</h1>")

def productView(request):
    return HttpResponse("<h1>Product View eKommerce</h1>")

def checkout(request):
    return HttpResponse("<h1>Checkout eKommerce</h1>")