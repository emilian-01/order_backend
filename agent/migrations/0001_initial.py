# Generated by Django 3.1.6 on 2021-02-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itw_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('deleted', models.BinaryField(default=b'0')),
            ],
        ),
    ]