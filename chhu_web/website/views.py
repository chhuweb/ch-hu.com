# -*- coding:utf-8 -*-

from django.shortcuts import render

def homepage_view(request):
    to_return = {'posts': 'Test'}
    return render(request, 'index.html', to_return)
