from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
    # return HttpResponse("<h1>Index Shop</h1>")