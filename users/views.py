import logging
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

logger = logging.getLogger(__name__)  # Create a logger for this module

def register_user(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("pets:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("pets:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("pets:list")
