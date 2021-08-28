from django.db.models import fields
import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *

class autoFilter(django_filters.FilterSet):
    # nr_rejestracyjny = CharFilter(field_name="nr_rejestracyjny",lookup_expr="icontains")
    # marka = CharFilter(field_name="marka",lookup_expr="icontains")
    # rok_produkcji = NumberFilter(field_name="rok_produkcji",lookup_expr="gte")
    # pesel = CharFilter(field_name="pesel", lookup_expr="icontains")

    class Meta:
        model = auto
        fields = {
            'nr_rejestracyjny':['icontains'],
            'marka':['icontains'],
            'rok_produkcji':['gte','lte'],
            'pesel':['icontains']
        }