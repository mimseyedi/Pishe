from django.db import models


class PaperCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته بندی")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'{self.id} - {self.name}'


class PaperTag(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام برچسب")

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Paper(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', verbose_name="عکس")
    title = models.CharField(max_length=300, verbose_name="تیتر")
    content = models.TextField(verbose_name="محتوا")
    category = models.ManyToManyField(PaperCategory, verbose_name="دسته بندی ها")
    tag = models.ManyToManyField(PaperTag, verbose_name="برچسب ها")
    counted_views = models.IntegerField(default=0, verbose_name="تعداد بازدید")
    status = models.BooleanField(default=False, verbose_name="وضعیت انتشار")
    published_date = models.DateTimeField(null=True, verbose_name="تاریخ انتشار")
    created_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_date = models.DateTimeField(null=True, auto_now=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return f'{self.id} - {self.title}'
