from django.contrib import admin
from django.urls import path, include
from website.views import home_view, about_view, contact_view, newsletters_view


urlpatterns = [
    path('', home_view, name="home"),
    path('about', about_view, name="about"),
    path('contact', contact_view, name="contact"),
    path('newsletters', newsletters_view, name="newsletters")
]