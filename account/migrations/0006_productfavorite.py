# Generated by Django 3.2.4 on 2022-04-26 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_cart_product'),
        ('account', '0005_delete_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book', unique=True, verbose_name='شناسه کتاب')),
            ],
            options={
                'verbose_name': 'نشان شده ها',
                'verbose_name_plural': 'نشان شده ها',
                'ordering': ['-created_date'],
            },
        ),
    ]
