from django.urls import path
from . import views

urlpatterns=[
    path('', views.restaurantHomePageView, name='Home'),
    path('cart', views.restaurantUserMGTPageView, name='User Management'),
    path('orders', views.restaurantOrderMGTPageView, name='Order Management'),
    path('aboutUs', views.restaurantFeedbackMGTPageView, name='Feedbacks Management'),

]