from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته بندی")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.id} - {self.name}'


class BlogTag(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام برچسب")

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="نویسنده")
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', verbose_name="عکس")
    title = models.CharField(max_length=300, verbose_name="تیتر")
    content = models.TextField(verbose_name="محتوا")
    category = models.ManyToManyField(BlogCategory, verbose_name="دسته بندی ها")
    tag = models.ManyToManyField(BlogTag, verbose_name="برچسب ها")
    counted_views = models.IntegerField(default=0, verbose_name="تعداد بازدید")
    status = models.BooleanField(default=False, verbose_name="وضعیت انتشار")
    published_date = models.DateTimeField(null=True, verbose_name="تاریخ انتشار")
    created_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(null=True, auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="شناسه پست")
    name = models.CharField(max_length=200, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیغام")
    approved = models.BooleanField(default=False, verbose_name="وضعیت تایید")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.id} - {self.name}'

