from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('auta/', views.auta ,name = "auta"),
    path('test/', views.test, name= "test")
]