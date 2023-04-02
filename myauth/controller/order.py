import json
from django.shortcuts import render, redirect
from django.contrib import messages
from myauth.forms import CustomUserForm
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from myauth.models import Order, OrderItem
from django.contrib.auth.decorators import login_required


def index(request):
    orders =Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, "myauth/orders/index.html", context)

def vieworder(request,t_no):
    order = Order.objects.filter(tracking_no =t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context ={'order':order, 'orderitems':orderitems}
    return render(request, "myauth/orders/view.html", context)