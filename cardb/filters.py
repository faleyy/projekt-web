from django.db.models import fields
from django.forms import widgets
import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *
from django.forms.widgets import DateInput
from django_filters.widgets import RangeWidget


class autoFilter(django_filters.FilterSet):
    class Meta:
        model = auto
        fields = {
            "nr_rejestracyjny": ["icontains"],
            "marka": ["icontains"],
            "rok_produkcji": ["gte", "lte"],
            "pesel": ["icontains"],
        }


class osobaFilter(django_filters.FilterSet):
    class Meta:
        model = osoba
        fields = {
            "pesel": ["icontains"],
            "imie": ["icontains"],
            "nazwisko": ["icontains"],
            "typ_miejscowosci": ["iexact"],
        }


class wypadekFilter(django_filters.FilterSet):
    data_wypadku__gte = django_filters.DateFilter(
        widget=DateInput(attrs={"type": "date"}),
        lookup_expr="gte",
        field_name="data_wypadku",
    )
    data_wypadku__lte = django_filters.DateFilter(
        widget=DateInput(attrs={"type": "date"}),
        lookup_expr="lte",
        field_name="data_wypadku",
    )

    class Meta:
        model = wypadek
        fields = {
            "wypadekid": ["icontains"],
            # "data_wypadku": ["gte", "lte"],
            "nr_rejestracyjny": ["icontains"],
            "wartosc_straty": ["gte", "lte"],
        }
