from django.urls import path
from . import views

urlpatterns=[
    path('foodAdmin', views.adminhomePageView, name='Admin Home'),
    path('foodAdmin/users', views.adminUserMGTPageView, name='User Management'),
    path('foodAdmin/orders', views.adminOrderMGTPageView, name='Order Management'),
    path('foodAdmin/feedback', views.adminFeedbackMGTPageView, name='Feedbacks Management'),

]