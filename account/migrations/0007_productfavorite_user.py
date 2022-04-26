# Generated by Django 3.2.4 on 2022-04-26 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_productfavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfavorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر'),
        ),
    ]
