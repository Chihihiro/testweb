from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    # home_page = 'C:\\Users\\qinxd\\Desktop\\910322113432153363.jpg'
    return render(request, 'home.html')



def hello(request):
    return HttpResponse("嘎嘎嘎嘎嘎萌哎萌哎啾咪o(*////▽////*)q")
