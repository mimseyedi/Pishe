from django.contrib import admin
from website.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('name', 'subject', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'email', 'content')
