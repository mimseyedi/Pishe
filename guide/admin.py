from django.contrib import admin
from guide.models import Paper, PaperCategory, PaperTag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Paper)
class PaperAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('title', 'counted_views', 'status', 'created_date', 'published_date')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(PaperCategory)
class PaperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(PaperTag)
class PaperTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)