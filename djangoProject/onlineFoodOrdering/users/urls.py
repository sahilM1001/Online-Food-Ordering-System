from django.urls import path
from . import views

urlpatterns=[
    path('', views.userHomePageView, name='Home'),
    path('cart', views.userCartPageView, name='User Management'),
    path('orders', views.userOrderMGTPageView, name='Order Management'),
    path('aboutUs', views.userAboutUsPageView, name='Feedbacks Management'),

]