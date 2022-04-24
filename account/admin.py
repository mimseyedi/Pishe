from django.contrib import admin
from account.models import UserInfo


@admin.register(UserInfo)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-EMPTY-"
    list_display = ('meli_code', 'mobile_phone', 'state', 'city', 'post_code', 'created_date')
    list_filter = ('city',)
    search_fields = ('meli_code', 'post_code')
