from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm, PasswordResetForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from account.models import UserInfo, ProductFavorite
from account.forms import UserInfoForm
from django.contrib.auth.models import User
from bookstore.models import Cart, Product, Order
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from random import randint


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("account_info"))
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نمی باشد!')


    form = AuthenticationForm()
    contect = {"form": form}
    return render(request, "account/login.html", contect)


def logout_view(request):
    if request.user.is_authenticated:
        product = Product.objects.all()
        product.delete()
        user_cart = Cart.objects.get(user=request.user)
        user_cart.total_price = 0
        user_cart.save()
        logout(request)
        return redirect('/')
    else:
        return HttpResponseRedirect(reverse("login"))


def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = User.objects.get(username=request.POST.get("username"))
                user.email = request.POST.get("email")
                user.save()

                user_info = UserInfo()
                user_info.user = user
                user_info.firstname = "n"
                user_info.lastname = "n"
                user_info.meli_code = "n"
                user_info.mobile_phone = "n"
                user_info.home_phone = "n"
                user_info.post_code = "n"
                user_info.address = "n"
                user_info.state = "n"
                user_info.city = "n"
                user_info.save()

                user_cart = Cart()
                user_cart.user = User.objects.get(username=request.POST.get("username"))
                user_cart.is_paid = False
                user_cart.order_id = randint(10000, 100000)
                user_cart.save()
                return HttpResponseRedirect(reverse("login"))

        return render(request, "account/signup.html")


def reset_password_view(request):
    msg = ''
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "بازیابی رمز عبور شما - وبسایت پیشه"
                    email_template_name = "account/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'mim.seyedi@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        msg = "ایمیل وارد شده صحیح نمی باشد!"

                    return HttpResponseRedirect(reverse("password_sent"))

    return render(request, "account/reset-password.html", {"msg": msg})


def password_sent_view(request):
    return render(request, "account/password_sent.html")


def password_reset_confirm_view(request):
    return render(request, "account/password_reset_confirm.html")


def password_reset_done_view(request):
    return render(request, "account/password_reset_done.html")


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
        msg = ''

        if request.method == "POST":
            if 'update_submit' in request.POST:
                form = UserInfoForm(request.POST, instance=current_user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نیست!')

            elif 'change_pass_submit' in request.POST:
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    msg = ''
                    return HttpResponseRedirect(reverse("pass_changed"))
                else:
                    msg = "اطلاعات وارد شده برای تغییر رمز صحیح نمی باشد. لطفا دوباره تلاش کنید!"

            elif 'delete_submit' in request.POST:
                user = User.objects.get(username=request.user.username)
                user.delete()
                return HttpResponseRedirect(reverse("account_del"))

        context = {"current_user": current_user, "msg": msg}
        return render(request, "account/account-setting.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def pass_changed_view(request):
    logout(request)
    return render(request, "account/pass_change.html")


def account_deleted_view(request):
    logout(request)
    return render(request, "account/delete_account.html")


def account_favorite_view(request):
    if request.user.is_authenticated:
        current_user = get_object_or_404(UserInfo, user=request.user.pk)
        products_fav = ProductFavorite.objects.filter(user=request.user.pk)

        context = {"current_user": current_user, "products_fav": products_fav}
        return render(request, "account/account-favorite.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def account_orders_view(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)

        context = {"orders": orders}
        return render(request, "account/account-orders.html", context)
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
                    user = User.objects.get(username=request.user.username)
                    user.first_name = request.POST.get("firstname")
                    user.last_name = request.POST.get("lastname")
                    user.save()
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نیست!')

            context = {"userinfo": current_user}
            return render(request, "account/account-information.html", context)

        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("login"))