from django.contrib import admin
from django.urls import path, include
from blog.views import blog_home_view

urlpatterns = [
    path('', blog_home_view, name="blog"),
    path('blog_category/<str:cat_name>', blog_home_view, name="blog_category"),
    path('blog_tag/<str:tag_name>', blog_home_view, name="blog_tag"),
]