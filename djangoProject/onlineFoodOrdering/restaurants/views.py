from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Admin Page Views START HERE
def restaurantHomePageView(request):
    return HttpResponse("Welcome to Restaurant Home")

def restaurantUserMGTPageView(request):
    return HttpResponse("Welcome to restaurant Management")

def restaurantOrderMGTPageView(request):
    return HttpResponse("Welcome to restaurant Orders page")

def restaurantFeedbackMGTPageView(request):
    return HttpResponse("Welcome to restaurant feedbacks page")

#Admin Page Views END HERE

