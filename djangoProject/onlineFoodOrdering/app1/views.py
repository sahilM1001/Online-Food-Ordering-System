from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Admin Page Views START HERE
def adminhomePageView(request):

    return HttpResponse("Welcome to admin Home")

def adminUserMGTPageView(request):
    return HttpResponse("Welcome to User Management")

def adminOrderMGTPageView(request):
    return HttpResponse("Welcome to Orders page")

def adminFeedbackMGTPageView(request):
    return HttpResponse("Welcome to Orders page")

#Admin Page Views END HERE

