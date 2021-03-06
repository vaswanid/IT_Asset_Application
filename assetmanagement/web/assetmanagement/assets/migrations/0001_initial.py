# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 20:13
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_from', models.DateField(verbose_name='Start date')),
                ('date_to', models.DateField(verbose_name='End Date')),
                ('notes', models.TextField(blank=True, null=True)),
                ('returned', models.BooleanField(default=False, verbose_name='Device Returned?')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('asset_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('serial_num', models.CharField(max_length=50)),
                ('passcode', models.CharField(max_length=50)),
                ('os_name', models.CharField(choices=[('ANDROID', 'Android'), ('IOS', 'iOS'), ('WIN', 'Windows Phone'), ('BB', 'BlackBerry'), ('OSX', 'OSX'), ('OTHER', 'Other (Specify in Notes)')], max_length=7)),
                ('os_version', models.CharField(max_length=50)),
                ('rooted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('SC', 'Security Consultant'), ('EC', 'Delivery Manager')], max_length=2)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Location', verbose_name='Base Office')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Location'),
        ),
        migrations.AddField(
            model_name='booking',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Device'),
        ),
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Person'),
        ),
    ]
