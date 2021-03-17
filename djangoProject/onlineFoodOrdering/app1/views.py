from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

##import mysql.connector as mcdb
##conn = mcdb.connect(host="localhost", user="root", passwd="", database="onlinefooddeliverysystem")
##print("successfully connected to db")

##cur = conn.cursor()
# Create your views here.

#Admin Page Views START HERE
def adminhomePageView(request):
    return render(request, 'admin/adminMaster.html')

def adminUserMGTPageView(request):
    return render(request, 'admin/user.html')

def adminUserAddView(request):
    return render(request, 'admin/addUser.html')

def adminOrderMGTPageView(request):
    return render(request, 'admin/order.html')

def adminFeedbackMGTPageView(request):

    ##cur.execute("SELECT * FROM ` tbl_feedbacks`")

    ##data = cur.fetchall()
    ##print(list(data))
    
    return render(request, 'admin/feedback.html')

#Admin Page Views END HERE

