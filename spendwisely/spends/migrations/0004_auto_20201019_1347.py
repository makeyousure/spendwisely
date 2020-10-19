# Generated by Django 3.1.2 on 2020-10-19 10:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spends', '0003_auto_20201011_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeoperation',
            name='income_acount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spends.account', verbose_name='Счет зачисления'),
        ),
        migrations.AlterField(
            model_name='incomeoperation',
            name='income_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 10, 47, 33, 957977, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='spendoperation',
            name='spend_acount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spends.account', verbose_name='Счет списания'),
        ),
        migrations.AlterField(
            model_name='spendoperation',
            name='spend_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 10, 47, 33, 957977, tzinfo=utc), verbose_name='Дата'),
        ),
    ]