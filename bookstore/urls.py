from django.contrib import admin
from django.urls import path, include
from bookstore.views import bookstore_home_view

urlpatterns = [
    path('', bookstore_home_view, name="bookstore_home"),

]