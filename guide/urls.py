from django.contrib import admin
from django.urls import path, include
from guide.views import guide_home_view

urlpatterns = [
    path('', guide_home_view, name="guide"),
    path('guide_category/<str:cat_name>', guide_home_view, name="guide_category"),
    path('guide_tag/<str:tag_name>', guide_home_view, name="guide_tag"),
]