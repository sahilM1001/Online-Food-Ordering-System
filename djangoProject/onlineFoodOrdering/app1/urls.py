from django.urls import path
from . import views

urlpatterns=[
    path('', views.adminhomePageView, name='Admin Home'),
    path('/view-users', views.adminUserMGTPageView, name='User Management'),
    path('/view-orders', views.adminOrderMGTPageView, name='Order Management'),
    path('/view-feedbacks', views.feedbacklisting, name='Feedbacks Management'),

]