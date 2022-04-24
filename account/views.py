from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نمی باشد!')


    form = AuthenticationForm()
    contect = {"form": form}
    return render(request, "account/login.html", contect)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponseRedirect(reverse("login"))


def signup_view(request):
    return render(request, "account/signup.html")


def reset_password_view(request):
    return render(request, "account/reset-password.html")


def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, "account/dashboard.html")
    else:
        return HttpResponseRedirect(reverse("login"))