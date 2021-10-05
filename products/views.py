from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'product': products})


def new(request):
    return HttpResponse('New Products.')
