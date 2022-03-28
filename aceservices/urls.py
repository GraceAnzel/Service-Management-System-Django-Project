from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Homepage"),
    path("about", views.about, name="AboutUs"),
    path("contact", views.contact, name="Contact"),
    path("product", views.product, name="Product"),
    #path("register", views.register, name="Register"),
    path("register",views.userregistration,name="reg"),
    path('login/',views.loginpage,name='login'),
    path("sform/",views.service1,name="service1"),
    path("service/", views.service, name="Service"),
    path("pay/",views.payment,name="payment"),
path('data1', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),




]
