from django.contrib import admin
from django.urls import path, include
from guide.views import guide_home_view, guide_single_view, guide_search_view

urlpatterns = [
    path('', guide_home_view, name="guide"),
    path('<int:paper_id>', guide_single_view, name="guide_single"),
    path('guide_category/<str:cat_name>', guide_home_view, name="guide_category"),
    path('guide_tag/<str:tag_name>', guide_home_view, name="guide_tag"),
    path('search/', guide_search_view, name="guide_search"),
]