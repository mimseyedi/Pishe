from django.contrib import admin
from blog.models import Post, BlogCategory, BlogTag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('title', 'counted_views', 'status', 'created_date', 'published_date')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)