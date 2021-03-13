from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#Admin Page Views START HERE
def loginPage(request):
    return render(request, 'login/login.html')

def signupPage(request):
    return render(request, 'login/signup.html')

#Admin Page Views END HERE

