from django.urls import path
from . import views

app_name='store'
urlpatterns=[
    path('', views.index, name='index'),
    path('new/', views.new, name='create' ),
    path('detail/<int:id>/',views.detail_item,name='detail'),
    
]