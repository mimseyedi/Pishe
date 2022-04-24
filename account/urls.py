from django.contrib import admin
from django.urls import path, include
from account.views import login_view, logout_view, signup_view, reset_password_view, dashboard_view

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup_view, name="signup"),
    path('reset_password', reset_password_view, name="reset_password"),
    path('dashboard', dashboard_view, name="dashboard"),
]