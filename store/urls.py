from django.urls import path
from . import views

app_name='store'
urlpatterns=[
    path('', views.index, name='index'),
    path('', views.items, name='items'),
    path('new/', views.new, name='create' ),
    path('detail/<int:id>/',views.detail_item,name='detail'),
    path('update/<int:id>/',views.update_item,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

    
]