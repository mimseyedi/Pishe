from django.db import models


class BookStoreCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته بندی")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان کتاب")
    image = models.ImageField(upload_to='bookstore/', default='bookstore/default.jpg', verbose_name="عکس")
    author = models.CharField(max_length=300, verbose_name="نویسنده")
    translator = models.CharField(max_length=300, verbose_name="مترجم")
    publication = models.CharField(max_length=300, verbose_name="نشر")
    price = models.FloatField(verbose_name="قیمت (به تومان)")
    description = models.TextField(verbose_name="توضیحات")
    category = models.ManyToManyField(BookStoreCategory, verbose_name="دسته بندی")
    shabak = models.CharField(max_length=300, verbose_name="شابک")
    published_date = models.DateTimeField(null=True, verbose_name="تاریخ انتشار")
    created_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(null=True, auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    def __str__(self):
        return f'{self.id} - {self.title}'


class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="شناسه کتاب")
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