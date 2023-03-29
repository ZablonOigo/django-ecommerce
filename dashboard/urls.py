from django.urls import path 
from . import views

app_name='dashboard'

urlpatterns=[
    path('dash/', views.index,name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
]