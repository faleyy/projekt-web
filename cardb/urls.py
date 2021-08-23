from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('auta/', views.auta ,name = "auta"),
    path('',views.index, name = "index")
]