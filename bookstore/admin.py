from django.contrib import admin
from bookstore.models import Book, BookStoreCategory, BookComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('title', 'author', 'translator', 'price', 'created_date', 'published_date')
    list_filter = ('category',)
    search_fields = ('title', 'author')
    summernote_fields = ('description',)


@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('email', 'approved', 'created_date', 'updated_date')
    search_fields = ('name', 'email')
    list_filter = ('approved',)


@admin.register(BookStoreCategory)
class BookStoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


