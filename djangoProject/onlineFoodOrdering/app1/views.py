from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Admin Page Views START HERE
def adminhomePageView(request):
    return render(request, 'app1/trialSetup1.html')

def adminUserMGTPageView(request):
    return HttpResponse("Welcome to admin User Management")

def adminOrderMGTPageView(request):
    return HttpResponse("Welcome to admin Orders page")

def adminFeedbackMGTPageView(request):
    return HttpResponse("Welcome to admin feedbacks page")

#Admin Page Views END HERE

