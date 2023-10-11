from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('product', views.product, name='product'),
    path('delivery', views.delivery, name='delivery'),
    path('inf', views.inf, name='inf'),
    path('contact', views.contact, name='contact'),
    path('voiti', views.voiti, name='voiti'),
    path('registr', views.registr, name='registr'),
]