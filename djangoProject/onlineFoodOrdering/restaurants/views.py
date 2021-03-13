from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#restaurant Page Views START HERE
def restaurantHomePageView(request):
    return render(request, 'restaurants/trailSetup2.html')

def restaurantFoodItemPageView(request):
    return HttpResponse("Welcome to restaurant food items Management")

def restaurantOrderMGTPageView(request):
    return HttpResponse("Welcome to restaurant Orders page")

def restaurantFeedbackMGTPageView(request):
    return HttpResponse("Welcome to restaurant feedbacks page")

#restaurant Page Views END HERE

