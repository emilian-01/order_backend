# Generated by Django 3.1.6 on 2021-02-19 11:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('order', '0003_auto_20210216_2154'),
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='itw_customer',
            new_name='Customer',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
        migrations.AlterModelTable(
            name='customer',
            table='itw_customer',
        ),
    ]