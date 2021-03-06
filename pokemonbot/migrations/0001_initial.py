# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_email', models.URLField(verbose_name='your google email')),
                ('google_password', models.CharField(max_length=10, verbose_name='your password')),
                ('location_lon', models.DecimalField(decimal_places=6, default=59.333409, max_digits=8, verbose_name='your current longitude')),
                ('location_lat', models.DecimalField(decimal_places=6, default=18.045008, help_text='this info your can find                                     on http://mondeca.com/index.php/en/any-place-en', max_digits=8, verbose_name='your current latitude')),
                ('gmapkey', models.CharField(help_text='this api key your can get on                     https://developers.google.com/maps/documentation/geocoding/get-api-key?hl=en', max_length=100, verbose_name='your password')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]
