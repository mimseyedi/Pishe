from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=300, verbose_name="موضوع")
    content = models.TextField(verbose_name="محتوا")
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تازیخ ساخت")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="تاریخ بروز رسانی")

    class Meta:
        ordering = ['created_date']
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return f'{self.name} - {self.subject}'


class NewsLetters(models.Model):
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'خبرنامه'

    def __str__(self):
        return f'{self.id} - {self.email}'
