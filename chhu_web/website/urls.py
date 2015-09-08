from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^$', 'website.views.homepage_view'),
)
