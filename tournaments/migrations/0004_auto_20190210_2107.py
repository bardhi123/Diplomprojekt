# Generated by Django 2.1.3 on 2019-02-10 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20190120_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='tourn_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 11, 20, 7, 30, 400509, tzinfo=utc)),
        ),
    ]