from django.shortcuts import render
from .models import auto

def auta(request):
    data = auto.objects.all()
    return render(request, 'auta.html', {"auta":data})
def test(request):
    return render(request, 'test.html',{})