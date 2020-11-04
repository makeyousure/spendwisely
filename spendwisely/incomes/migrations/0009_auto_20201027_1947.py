# Generated by Django 3.1.2 on 2020-10-27 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0008_auto_20201027_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeoperation',
            name='income_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 16, 47, 1, 637309, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='spendoperation',
            name='spend_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 16, 47, 1, 637309, tzinfo=utc), verbose_name='Дата'),
        ),
    ]
