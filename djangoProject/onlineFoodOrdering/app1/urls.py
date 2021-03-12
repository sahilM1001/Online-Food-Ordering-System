from django.urls import path
from . import views

urlpatterns=[
    path('', views.adminhomePageView, name='Admin Home'),
    path('users', views.adminUserMGTPageView, name='User Management'),
    path('orders', views.adminOrderMGTPageView, name='Order Management'),
    path('feedback', views.adminFeedbackMGTPageView, name='Feedbacks Management'),
]