from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    # home_page = 'C:\\Users\\qinxd\\Desktop\\910322113432153363.jpg'
    if request.method == 'POST':
        # new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})






def hello(request):
    return HttpResponse("嘎嘎嘎嘎嘎萌哎萌哎啾咪o(*////▽////*)q")
