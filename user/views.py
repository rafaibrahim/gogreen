from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request): 
    return render(request, 'user/login.html')
 
def home(request): 
    return render(request, 'user/home.html')

def cart(request): 
    return render(request, 'user/cart.html')

def payment(request): 
    return render(request, 'user/payment.html')




 
