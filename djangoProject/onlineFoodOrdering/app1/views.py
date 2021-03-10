from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Admin Page Views START HERE
def adminhomePageView(request):
    return render(request, 'index.html')

def adminUserMGTPageView(request):
    return render(request, 'user.html')

def adminOrderMGTPageView(request):
    return render(request, 'order.html')

def adminFeedbackMGTPageView(request):
    return render(request, 'feedback.html')

#Admin Page Views END HERE

