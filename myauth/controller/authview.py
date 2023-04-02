from django.shortcuts import render, redirect
from django.contrib import messages
from myauth.forms import CustomUserForm
from django.contrib.auth import login, logout, authenticate

def register(request):
    form = CustomUserForm()
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully ! Login to Continue")
            return redirect('/login')
    context ={'form':form}
    return render(request, "myauth/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already Logged in")
        return redirect('/')
   
    else:
        if request.method =='POST':
            phone =request.POST.get('phone')
            passwd =request.POST.get('password')

            user = authenticate(request, phone=phone, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Sucesfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Mobile No or Password")
                return redirect('/login')
        return render(request, "myauth/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
    return redirect ("/")

