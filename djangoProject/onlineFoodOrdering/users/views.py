
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#User Page Views START HERE
def userHomePageView(request):
    return render(request, 'users/userMaster.html')

def UserhomeMGTPageView(request):
    return render(request, 'users/index.html')    

def userCartPageView(request):
    return render(request, 'users/cart.html')

def userCheckoutPageView(request):
    return render(request, 'users/checkout.html')

def userAboutUsPageView(request):
    return render(request, 'users/about-us.html')

def userMenuGridPageView(request):
    return render(request, 'users/menu-grid.html')

def usercontactPageView(request):
    return render(request, 'users/contact.html')

def userservicePageView(request):
    return render(request, 'users/service.html')

def usergalleryPageView(request):
    return render(request, 'users/gallery.html')
#User Page Views END HERE

