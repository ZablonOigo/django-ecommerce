from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from.forms import *
from django.contrib .auth.decorators import login_required
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

@login_required
def new(request):
    if request.method =='GET':
       context={'form':Newform()}
       return render(request,'store/new_item.html', context)
    elif request.method =='POST':
        form=Newform(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('store:detail',id=item.id)
    else:
        form=Newform()
    return render(request,'store/new_item.html',{'form':form})
    #    if request.method =='POST':
    #   form=Newform(request.POST, request.FILES)
    #   if form.is_valid():
    #       item=form.save(commit=False)
    #       item.created_by=request.user
    #       item.save()
    #       return redirect('store:detail', pk=item.id)
    #   else:
    #    form=Newform()
    #    context={'form':form}
    #    return render(request,'store/new_item.html',{'form':form})

