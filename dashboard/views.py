from django.shortcuts import render,redirect,get_object_or_404
from store.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)
    context={'items':items}
    return render(request,'dashboard/index.html',context)

@login_required
def delete(request,id):
    item=get_object_or_404(Item,id=id,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
