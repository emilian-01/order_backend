# Generated by Django 3.1.6 on 2021-02-16 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('order', '0002_auto_20210216_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itw_order',
            name='date_registered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
