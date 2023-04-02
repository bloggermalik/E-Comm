
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
# Create your views here.
def home(request):
    category = Category.objects.filter(status = 0)
    context = {
        "category":category
    }
    return render(request, "myauth/index.html", context)

def collections(request):
    category = Category.objects.filter(status = 0)
    context = {
        "category":category
    }
    return render(request, "myauth/collections.html", context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug, status =0)):
        products = Product.objects.filter(category__slug=slug)
        category =Category.objects.filter(slug=slug).first()
        context = {
            'products':products, 
            'category':category
            }

        return render(request, "myauth/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview (request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status =0)):
        if(Product.objects.filter(slug=prod_slug, status =0)):
            products = Product.objects.filter(slug=prod_slug, status =0).first
            context = {"products":products}
        else:
            messages.error(request, "No Such Product Found")
            return redirect('collections')

    else:
        messages.error(request,"No such category found")
        return redirect('collections')
    return render(request, "myauth/products/view.html", context)

def viewcart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        context = {'cart':cart}
        return render (request, "myauth/cart.html", context)
    else:
        return redirect('loginpage')

def updatecart(request):
    if request.method =='POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user= request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
    return redirect('/')

def myaccount(request):
    category = Category.objects.filter(status = 0)
    context = {
        "category":category
    }
    return render(request, "myauth/myaccount.html", context)