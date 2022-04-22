# Generated by Django 3.2.4 on 2022-04-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان کتاب')),
                ('image', models.ImageField(default='bookstore/default.jpg', upload_to='bookstore/', verbose_name='عکس')),
                ('author', models.CharField(max_length=300, verbose_name='نویسنده')),
                ('translator', models.CharField(max_length=300, verbose_name='مترجم')),
                ('publication', models.CharField(max_length=300, verbose_name='نشر')),
                ('price', models.FloatField(verbose_name='قیمت (به تومان)')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('shabak', models.CharField(max_length=300, verbose_name='شابک')),
                ('published_date', models.DateTimeField(null=True, verbose_name='تاریخ انتشار')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروز رسانی')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='BookStoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='پیغام')),
                ('approved', models.BooleanField(default=False, verbose_name='وضعیت تایید')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book', verbose_name='شناسه کتاب')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='bookstore.BookStoreCategory', verbose_name='دسته بندی'),
        ),
    ]