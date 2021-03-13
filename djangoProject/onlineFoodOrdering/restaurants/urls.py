from django.urls import path
from . import views

urlpatterns=[
    path('', views.restaurantHomePageView, name='Home'),
    path('/foodItems', views.restaurantFoodItemPageView, name='User Management'),
    path('/orders', views.restaurantOrderMGTPageView, name='Order Management'),
    path('/feedback', views.restaurantFeedbackMGTPageView, name='Feedbacks Management'),

]