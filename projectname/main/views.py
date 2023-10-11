from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def product(request):
    return render(request, 'main/product.html')


def delivery(request):
    return render(request, 'main/delivery.html')


def inf(request):
    return render(request, 'main/inf.html')


def contact(request):
    return render(request, 'main/contact.html')


def voiti(request):
    return render(request, 'main/voiti.html')


def registr(request):
    return render(request, 'main/registr.html')


