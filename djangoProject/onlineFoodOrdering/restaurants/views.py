from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#restaurant Page Views START HERE
def restaurantHomePageView(request):
    return render(request, 'restaurants/restaurantMaster.html')

def restaurantFoodItemPageView(request):
    return render(request, 'restaurants/index.html')

def restaurantOrderMGTPageView(request):
    return render(request, 'restaurants/order.html')

def restaurantDeliveryMGTPageView(request):
    return render(request, 'restaurants/delivery.html')

def restaurantFeedbackMGTPageView(request):
    return render(request, 'restaurants/feedback.html')

#restaurant Page Views END HERE

