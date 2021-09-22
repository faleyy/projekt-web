from django.db import models


class osoba(models.Model):
    pesel = models.CharField(max_length=11, primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    typ_miejscowosci = models.CharField(max_length=1)

    class Meta:
        db_table = "osoby"


class auto(models.Model):
    nr_rejestracyjny = models.CharField(max_length=7, primary_key=True)
    marka = models.CharField(max_length=64)
    rok_produkcji = models.IntegerField()
    pesel = models.CharField(max_length=11)

    class Meta:
        db_table = "auta"


class wypadek(models.Model):
    wypadekid = models.IntegerField(db_column="wypadekID", primary_key=True)
    data_wypadku = models.DateField()
    nr_rejestracyjny = models.CharField(max_length=7)
    wartosc_straty = models.IntegerField()

    class Meta:
        db_table = "wypadki"
