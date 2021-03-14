from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Admin Page Views START HERE
def adminhomePageView(request):
    return render(request, 'admin/adminMaster.html')

def adminUserMGTPageView(request):
    return render(request, 'admin/user.html')

def adminOrderMGTPageView(request):
    return render(request, 'admin/order.html')

def adminFeedbackMGTPageView(request):
    return render(request, 'admin/feedback.html')

#Admin Page Views END HERE

