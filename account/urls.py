from django.contrib import admin
from django.urls import path, include
import account.views as views

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup_view, name="signup"),
    path('reset_password', views.reset_password_view, name="reset_password"),
    path('info', views.account_info_view, name="account_info"),
    path('dashboard', views.dashboard_view, name="dashboard"),
    path('setting', views.account_setting_view, name="account_sett"),
    path('favorite', views.account_favorite_view, name="account_fav"),
    path('password_changed', views.pass_changed_view, name="pass_changed"),
]