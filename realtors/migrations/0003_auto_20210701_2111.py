# Generated by Django 3.2.4 on 2021-07-01 15:41

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 1, 21, 11, 53, 366761)),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]