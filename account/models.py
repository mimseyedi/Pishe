from django.db import models
from django.contrib.auth.models import User
from bookstore.models import Book


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="شناسه کاربر")
    image = models.ImageField(upload_to='accounts/', default='accounts/default.png', verbose_name="آواتار")
    firstname = models.CharField(max_length=100, verbose_name="نام", null=True)
    lastname = models.CharField(max_length=100, verbose_name="نام خانوادگی", null=True)
    meli_code = models.CharField(max_length=100, verbose_name="کد ملی")
    mobile_phone = models.CharField(max_length=100, verbose_name="شماره موبایل")
    home_phone = models.CharField(max_length=100, verbose_name="شماره ثابت")
    post_code = models.CharField(max_length=100, verbose_name="کد پستی")
    address = models.TextField(verbose_name="نشانی")
    state = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'اطلاعات کاربر'
        verbose_name_plural = 'اطلاعات کاربر'

    def __str__(self):
        return f'{self.id} - {self.user}'


class ProductFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="شناسه کاربر")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="شناسه کتاب")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'نشان شده ها'
        verbose_name_plural = 'نشان شده ها'

    def __str__(self):
        return f'{self.id}'
