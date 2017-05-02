from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Category, Product


def home(request):
    return render(request, 'storeApp/home.html', {'categories': Category.objects.all(), 'products': Product.objects.all()})


def about_us(request):
    return render(request, 'storeApp/about_us.html', {})


def contact_us(request):
    return render(request, 'storeApp/contact_us.html', {})