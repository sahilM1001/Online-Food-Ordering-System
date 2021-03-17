from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='onlinefooddeliverysystem')
print('Successfully connected to database')
cur = conn.cursor()

#Admin Page Views START HERE
def adminhomePageView(request):
    return render(request, 'admin/adminMaster.html')

def adminUserMGTPageView(request):
    return render(request, 'admin/user.html')

def adminOrderMGTPageView(request):
    return render(request, 'admin/order.html')

def adminFeedbackMGTPageView(request):
    return render(request, 'admin/feedback.html')

def feedbacklisting(request):
    cur.execute("SELECT * FROM `tbl_feedbacks`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/feedback.html', {'feedback': data})

#Admin Page Views END HERE

