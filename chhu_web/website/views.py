# -*- coding:utf-8 -*-

from django.shortcuts import render

def homepage_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'index.html', to_return)


def about_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'about.html', to_return)

def contact_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'contact.html', to_return)

def services_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'services.html', to_return)

def price_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'price.html', to_return)