# Generated by Django 3.2.3 on 2021-07-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsessionmodel',
            name='login_time',
            field=models.DateTimeField(null=True),
        ),
    ]
