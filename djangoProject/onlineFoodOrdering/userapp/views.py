from django.shortcuts import render

# Create your views here.

#Admin Page Views START HERE
def userhomePageView(request):
    return render(request, 'UserSide/index.html')

def useraboutPageView(request):
    return render(request, 'UserSide/about.html')
