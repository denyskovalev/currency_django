# Generated by Django 4.0.6 on 2022-10-02 21:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 2, 21, 13, 6, 722545, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='source',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 2, 21, 13, 6, 721941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_name',
            field=models.CharField(choices=[('PrivatBank', 'Private Bank'), ('Monobank', 'Monobank'), ('Vkurse', 'Vkurse'), ('Oschadbank', 'Oschadbank'), ('Finance.ua', 'Finance.ua'), ('Ukrsibbank', 'Ukrsibbank')], max_length=16, unique=True),
        ),
    ]
