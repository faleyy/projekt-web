from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .models import auto, osoba, wypadek
from .filters import autoFilter, osobaFilter, wypadekFilter
from .forms import CreateUserForm


@login_required
def index(request):
    return render(request, "index.html", {})


def register(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("index")

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(
                request, "Użytkownik " + user + " został pomyślnie zarejestrowany!"
            )
            return redirect("login")
    return render(request, "register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            redirectPath = request.GET.get("next", "index")
            login(request, user)
            return redirect(redirectPath)
        else:
            messages.info(request, "Nazwa użytkownika lub hasło są nieprawidłowe")

    return render(request, "login.html", {})


def logoutUser(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany")
    return redirect("login")


@login_required
def profile(request):
    return render(request, "profile.html", {})


@login_required
def osoby(request):
    data = osoba.objects.all()
    myFilter = osobaFilter(request.GET, queryset=data)
    data = myFilter.qs
    mySort = request.GET.get("sortid", "pesel")
    data = data.order_by(mySort)
    return render(
        request, "osoby.html", {"osoby": data, "myFilter": myFilter, "mySort": mySort}
    )


@login_required
def auta(request):
    data = auto.objects.all()
    myFilter = autoFilter(request.GET, queryset=data)
    data = myFilter.qs
    mySort = request.GET.get("sortid", "nr_rejestracyjny")
    data = data.order_by(mySort)
    return render(
        request, "auta.html", {"auta": data, "myFilter": myFilter, "mySort": mySort}
    )


@login_required
def wypadki(request):
    data = wypadek.objects.all()
    myFilter = wypadekFilter(request.GET, queryset=data)
    data = myFilter.qs
    mySort = request.GET.get("sortid", "wypadekid")
    data = data.order_by(mySort)
    return render(
        request,
        "wypadki.html",
        {"wypadki": data, "myFilter": myFilter, "mySort": mySort},
    )
