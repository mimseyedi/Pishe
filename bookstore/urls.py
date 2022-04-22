from django.contrib import admin
from django.urls import path, include
from bookstore.views import bookstore_home_view, bookstore_single_view

urlpatterns = [
    path('', bookstore_home_view, name="bookstore_home"),
    path('<int:book_id>', bookstore_single_view, name="bookstore_single"),
    path('book_category/<str:cat_name>', bookstore_home_view, name="book_category"),
    path('search/', bookstore_home_view, name="bookstore_search"),
]