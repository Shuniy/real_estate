# Generated by Django 3.2.4 on 2021-07-03 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0014_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 58, 58, 449573)),
        ),
    ]
