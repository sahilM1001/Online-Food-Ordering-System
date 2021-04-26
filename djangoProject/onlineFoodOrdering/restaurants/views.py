from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='onlinefooddeliverysystem')
print('Successfully connected to database')
cur = conn.cursor()



#restaurant Page Views START HERE
def restaurantHomePageView(request):
    return render(request, 'restaurants/food.html')

def restaurantFoodItemPageView(request):
    cur.execute("SELECT * FROM `tbl_food_items`")
    data = cur.fetchall()
    print(list(data))

    return render(request, 'restaurants/food.html', {'items': data})


def restaurantOrderMGTPageView(request):

    cur.execute("SELECT * FROM `tbl_order_details`")
    data = cur.fetchall()

    print(list(data))
    return render(request, 'restaurants/order.html', {'orderDetails': data})

def restaurantDeliveryMGTPageView(request):
    
    cur.execute("SELECT * FROM `tbl_delivery`")
    data = cur.fetchall()

    print(list(data))
    return render(request, 'restaurants/delivery.html', {'deliveries': data})

def restaurantPaymentMGTPageView(request):

    cur.execute("SELECT * FROM `tbl_pyt`")
    data = cur.fetchall()

    print(list(data))

    return render(request, 'restaurants/pay.html', {'payments': data})


def restaurantFeedbackMGTPageView(request):
    return render(request, 'restaurants/feedback.html')

#restaurant Page Views END HERE

