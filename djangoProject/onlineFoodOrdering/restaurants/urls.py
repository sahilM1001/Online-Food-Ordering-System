from django.urls import path
from . import views

urlpatterns=[
    path('', views.restaurantHomePageView, name='Home'),
    path('/view-food', views.restaurantFoodItemPageView, name='Food Item Management'),
    path('/view-orders', views.restaurantOrderMGTPageView, name='Order Management'),
    path('/view-delivery', views.restaurantDeliveryMGTPageView, name='Delivery Management'),
    path('/view-feedback', views.restaurantFeedbackMGTPageView, name='Feedbacks Management'),
    path('/view-payment', views.restaurantPaymentMGTPageView, name='Payments Management'),

]