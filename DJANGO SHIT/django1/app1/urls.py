from django.urls import path
from app1 import views

urlpatterns = [ 
    path('index/', views.index),

    ]