from django.urls import path
from . import views

urlpatterns = [
    path('auta/', views.auta ,name = "auta")
]