from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name = "ecomapp"
urlpatterns = [
    path("",Homeview.as_view(),name="home"),
    path("about/",Aboutview.as_view(),name="about"),
    path("contact/",views.contact,name="contact"),
    path("allproducts/",Allproductview.as_view(),name="allproducts"),
    path("product/<slug:slug>/",Productdetailview.as_view(),name="productdetail"),
    path("add-to-cart-<int:pro_id>",Addtocartview.as_view(),name="addtocart"),
    path("mycart/", MycartView.as_view(), name="mycart"),
    path("managecart/<int:cp_id>/", Managecartview.as_view(), name="managecart"),
    path("checkout/", Checkoutview.as_view(), name="checkout"),
    path("register/",Registrationview.as_view(), name="registration"),
    path("login/", Loginview.as_view(), name="login"),
    path("logout/", Logoutview.as_view(), name="logout"),
    path("profile/", Profileview.as_view(), name="profile"),
    path("profile/order-<int:pk>/",Orderdetailview.as_view(),
         name="orderdetail"),
     path("search/", Searchview.as_view(), name="search"),
     path("forgotpassword/", forgotpasswordview.as_view(), name="forgotpassword"),
     path("password-reset/<email>/<token>/",
         Passwordresetview.as_view(), name="passwordreset"),


    ]