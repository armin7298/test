# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-30 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_melli_code', models.IntegerField()),
                ('account_number', models.IntegerField(unique=True)),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melli_code', models.IntegerField(unique=True)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CoreBanking.Center')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('melli_code', models.IntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('member_ship_type', models.CharField(blank=True, choices=[('head_manager', 'Head Manager'), ('legal_expert', 'Legal Expert'), ('bank_manager', 'Bank Manager'), ('center_manager', 'Center Manager'), ('cashier', 'Cashier'), ('auditor', 'Auditor'), ('accountant', 'Accountant')], max_length=20)),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CoreBanking.Center')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CoreBanking.Center'),
        ),
    ]
