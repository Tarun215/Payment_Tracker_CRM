# Generated by Django 3.2.3 on 2021-06-19 05:10

import client.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=12)),
                ('image', models.ImageField(blank=True, upload_to=client.models.client_upload_to)),
                ('account_holder_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=50)),
                ('MCIR_code', models.CharField(max_length=50)),
                ('IFSC_code', models.CharField(max_length=50)),
                ('name_of_bank', models.CharField(max_length=150)),
                ('client_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('postal_pin_code', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
