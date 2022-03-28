from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import RegistrationForm, GetService, Pay
from django.http import HttpResponse, request, HttpResponseRedirect
from django.core.mail import send_mail
from .models import User,add
from django.db.models import Q
import mimetypes
mimetypes.add_type("text/css", ".css", True)
from aceservices.models import Product
from .models import Category
from .models import Service
from django.core import serializers
from django.http import JsonResponse


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Product.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def payment(request):
    form_class = Pay
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            subject = 'Payment Confirmation'
            message = "Thank you for choosing our website. We got your payment and our staff will arrive soon.FROM ACESERVICES "
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('Service')
    return render(request,'payment.html',{'form': form})

def service(request):
    services = Service.get_all_services();
    return render(request, 'service.html', {'services': services})


def service1(request):
    form_class = GetService
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('payment')
    return render(request, 'form.html', {'form': form})
def userregistration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'welcome to Ace Services'
            message = "Thank you for registering in our website. We are hoping to give the best service for you."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'register.html',{'form':form})


def loginpage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        flag=User.objects.filter(Q(username=uname) & Q(password=pwd))
        if flag:
            #request.session['uname']=uname
            return redirect('Service')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')
    return render(request,"login.html")


def product(request):
    products = None
    categories = Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'product.html', data)





