from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from account.models import UserInfo
from account.forms import UserInfoForm
from django.contrib.auth.models import User
from hashlib import sha256


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
        current_user = get_object_or_404(UserInfo, user=request.user.pk)
        context = {"current_user": current_user}
        return render(request, "account/dashboard.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def account_setting_view(request):
    if request.user.is_authenticated:
        current_user = get_object_or_404(UserInfo, user=request.user.pk)

        if request.method == "POST":
            if 'update_submit' in request.POST:
                form = UserInfoForm(request.POST, instance=current_user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نیست!')

            elif 'change_pass_submit' in request.POST:
                old_pass = request.POST.get('last_pass')
                new_pass = request.POST.get('new_pass')
                new_pass_conf = request.POST.get('new_pass_conf')
                if new_pass == new_pass_conf:
                    user = User.objects.get(username__exact=request.user.username)
                    user.set_password(new_pass)
                    user.save()
                    logout(request)
                    return HttpResponseRedirect(reverse("pass_changed"))
                else:
                    messages.add_message(request, messages.ERROR, 'تاییدیه رمز با رمز جدید مطابقت ندارد!')
                    return HttpResponseRedirect(reverse("account_sett"))


        context = {"current_user": current_user}
        return render(request, "account/account-setting.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def pass_changed_view(request):
    return render(request, "account/pass_change.html")


def account_favorite_view(request):
    if request.user.is_authenticated:
        current_user = get_object_or_404(UserInfo, user=request.user.pk)
        context = {"current_user": current_user}
        return render(request, "account/account-favorite.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def account_info_view(request):
    current_user = get_object_or_404(UserInfo, user=request.user.pk)

    if request.user.is_authenticated:
        if current_user.firstname == 'n' and current_user.lastname == 'n' and \
                current_user.meli_code == 'n' and current_user.mobile_phone == 'n' and \
                current_user.home_phone == 'n' and current_user.post_code == 'n' and \
                current_user.address == 'n' and current_user.state == 'n' and \
                current_user.city == 'n':

            if request.method == "POST":
                form = UserInfoForm(request.POST, instance=current_user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نیست!')

            context = {"userinfo": current_user}
            return render(request, "account/account-information.html", context)

        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("login"))