from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='onlinefooddeliverysystem')
print('Successfully connected to database')
cur = conn.cursor()

#restaurant Page Views START HERE
def restaurantHomePageView(request):
    return render(request, 'restaurants/restaurantMaster.html')

def restaurantFoodItemPageView(request):
    return render(request, 'restaurants/food.html')


def restaurantOrderMGTPageView(request):
    return render(request, 'restaurants/order.html')

def restaurantDeliveryMGTPageView(request):
    return render(request, 'restaurants/delivery.html')

def restaurantPaymentMGTPageView(request):
    return render(request, 'restaurants/pay.html')


def restaurantFeedbackMGTPageView(request):
    return render(request, 'restaurants/feedback.html')

def deliverylisting(request):
    cur.execute("SELECT * FROM `tbl_delivery`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'restaurants/delivery.html', {'delivery': data})

def feedbacklisting(request):
    cur.execute("SELECT * FROM `tbl_feedbacks`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'restaurants/feedback.html', {'feedback': data})

def foodlisting(request):
    cur.execute("SELECT * FROM `tbl_food_items`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'restaurants/food.html', {'food': data})

def paymentlisting(request):
    cur.execute("SELECT * FROM `tbl_pyt`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'restaurants/pay.html', {'payment': data})

def orderlisting(request):
    cur.execute("SELECT * FROM `tbl_order_details`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'restaurants/order.html', {'order': data})

def foodaddcreate(request):
    return render(request, 'restaurants/addfood.html')   


def foodaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        foodid = request.POST['txt1']
        foodcategory = request.POST['txt2']
        foodname = request.POST['txt3']
        foodprice = request.POST['txt4']
        cur.execute("INSERT INTO `onlinefoodordering`(`f_id`,`category_name`,`f_name`,`f_price`) VALUES ('{}','{}','{}','{}')".format(foodid,foodcategory,foodname,foodprice))
        conn.commit()
        return redirect(foodaddcreate) 
    else:
        return redirect(foodaddcreate)

#restaurant Page Views END HERE

