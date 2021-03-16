from django.urls import path
from . import views

urlpatterns=[
    path('', views.userHomePageView, name='Home'),
    path('/view-index', views.UserhomeMGTPageView, name='index'),
    path('/cart', views.userCartPageView, name='cart'),
    path('/view-aboutUs', views.userAboutUsPageView, name='About-Us'),

]