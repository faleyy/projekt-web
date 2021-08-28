from django.shortcuts import render
from .models import auto
from .filters import autoFilter

def auta(request):
    data = auto.objects.all()
    myFilter = autoFilter(request.GET, queryset=data)
    data = myFilter.qs
    mySort = request.GET.get('sortid','nr_rejestracyjny')
    data = data.order_by(mySort)
    return render(request, 'auta.html', {"auta":data,"myFilter":myFilter,"mySort":mySort})


def index(request):
    return render(request, 'index.html',{})