# Generated by Django 3.1.6 on 2021-02-19 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210219_1739'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='itw_product',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='itw_product_category',
            new_name='ProductCategory',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'product_category', 'verbose_name_plural': 'product_categories'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='itw_product',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='itw_product_category',
        ),
    ]
