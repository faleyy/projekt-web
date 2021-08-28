from django.shortcuts import render
from .models import auto
from .filters import autoFilter

def auta(request):
    data = auto.objects.all()
    myFilter = autoFilter(request.GET, queryset=data)
    data = myFilter.qs

    return render(request, 'auta.html', {"auta":data,"myFilter":myFilter})


def index(request):
    return render(request, 'index.html',{})