# Generated by Django 3.2.3 on 2021-06-28 07:53

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('balance', models.CharField(max_length=50)),
                ('last_record', models.FileField(blank=True, upload_to=account.models.last_account_upload_to)),
                ('second_last_record', models.FileField(blank=True, upload_to=account.models.second_last_account_upload_to)),
            ],
        ),
    ]
