from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

 
def home(request): 
    return render(request, 'user/home.html')

def cart(request): 
    return render(request, 'user/cart.html')





 
