from django.shortcuts import render

def product_view(request):
    return render(request, 'product.html')

def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def cart_view(request):
    return render(request, 'cart.html')
# Create your views here.
