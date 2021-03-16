from django.urls import path
from . import views

urlpatterns=[
    path('', views.userHomePageView, name='Home'),
    path('/index', views.UserhomeMGTPageView, name='index'),
    path('/cart', views.userCartPageView, name='cart'),
    path('/about', views.userAboutUsPageView, name='About-Us'),
    path('/checkout', views.userCheckoutPageView, name='checkout'),
    path('/menu', views.userMenuGridPageView, name='menu-grid'),
    path('/contact', views.usercontactPageView, name='contact'),
    path('/service', views.userservicePageView, name='service'),
    path('/gallery', views.usergalleryPageView, name='gallery'),

]