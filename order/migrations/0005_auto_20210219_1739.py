# Generated by Django 3.1.6 on 2021-02-19 16:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20210219_1225'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('order', '0004_auto_20210219_1225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='itw_counter',
            new_name='Counter',
        ),
        migrations.RenameModel(
            old_name='itw_order',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='itw_order_unit',
            new_name='OrderUnit',
        ),
        migrations.AlterModelOptions(
            name='counter',
            options={'verbose_name': 'counter', 'verbose_name_plural': 'counters'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='orderunit',
            options={'verbose_name': 'order_unit', 'verbose_name_plural': 'order_units'},
        ),
        migrations.AlterModelTable(
            name='counter',
            table='itw_counter',
        ),
        migrations.AlterModelTable(
            name='order',
            table='itw_order',
        ),
        migrations.AlterModelTable(
            name='orderunit',
            table='itw_order_unit',
        ),
    ]
