# Generated by Django 2.1.3 on 2019-01-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190120_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
