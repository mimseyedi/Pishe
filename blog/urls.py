from django.contrib import admin
from django.urls import path, include
from blog.views import blog_home_view, blog_single_view

urlpatterns = [
    path('', blog_home_view, name="blog"),
    path('<int:post_id>', blog_single_view, name="blog_single"),
    path('blog_category/<str:cat_name>', blog_home_view, name="blog_category"),
    path('blog_tag/<str:tag_name>', blog_home_view, name="blog_tag"),
]