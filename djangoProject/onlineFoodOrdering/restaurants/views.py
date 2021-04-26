<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render,redirect
>>>>>>> eea31147b57b7c8c943da486ddc8b71d11f199c7
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='onlinefooddeliverysystem')
print('Successfully connected to database')
cur = conn.cursor()

<<<<<<< HEAD


=======
>>>>>>> eea31147b57b7c8c943da486ddc8b71d11f199c7
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

