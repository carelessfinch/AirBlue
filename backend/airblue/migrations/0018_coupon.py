# Generated by Django 3.2.4 on 2021-10-08 18:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airblue', '0017_items_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=1, verbose_name='coupon_value')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('blacklist_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
