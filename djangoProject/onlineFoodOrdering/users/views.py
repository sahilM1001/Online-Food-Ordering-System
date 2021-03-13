
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#User Page Views START HERE
def userHomePageView(request):
    return render(request, 'users/trialSetup3.html')

def userCartPageView(request):
    return HttpResponse("Welcome to User cart Management")

def userOrderMGTPageView(request):
    return HttpResponse("Welcome to user Orders page")

def userAboutUsPageView(request):
    return HttpResponse("Welcome to user About Us page")

#User Page Views END HERE

