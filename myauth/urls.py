from django.contrib import admin
from django.urls import path
from myauth import views
from myauth.controller import authview, cart, checkout, order
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),


    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', views.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),

    path('proceed-to-pay', checkout.razorpaycheck),

    path('my-orders', order.index, name="myorders"),

    path('view-order/<str:t_no>', order.vieworder, name="orderview"),
]




