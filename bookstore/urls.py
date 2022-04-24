from django.contrib import admin
from django.urls import path, include
from bookstore.views import bookstore_home_view, bookstore_single_view, checkout_view, cart_view

urlpatterns = [
    path('', bookstore_home_view, name="bookstore_home"),
    path('<int:book_id>', bookstore_single_view, name="bookstore_single"),
    path('book_category/<str:cat_name>', bookstore_home_view, name="book_category"),
    path('search/', bookstore_home_view, name="bookstore_search"),
    path('checkout/', checkout_view, name="checkout"),
    path('cart/', cart_view, name="cart"),
]