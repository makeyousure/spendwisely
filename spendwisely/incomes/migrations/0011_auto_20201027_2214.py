# Generated by Django 3.1.2 on 2020-10-27 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0010_auto_20201027_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeoperation',
            name='income_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 19, 14, 40, 64641, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='spendoperation',
            name='spend_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 19, 14, 40, 65639, tzinfo=utc), verbose_name='Дата'),
        ),
    ]