from django.urls import path
from . import views

urlpatterns=[
    path('', views.userhomePageView, name='userhomePageView'),
    path('about', views.useraboutPageView, name='useraboutPageView'),
]