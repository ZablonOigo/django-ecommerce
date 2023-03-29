from django.shortcuts import render,get_object_or_404
from.models import *
from.forms import *
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    context={'categories':categories, 'items':items}

    return render(request,'store/index.html',context)


def detail_item(request,id):
    item=get_object_or_404(Item,id=id)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(id=id)[0:3]
    context={'item':item,
             'related_items':related_items}
    return render(request,'store/detail_item.html',context)


def new(request):
    form=Newform()
    context={'form':form}
    return render(request,'store/new_item.html',context)
