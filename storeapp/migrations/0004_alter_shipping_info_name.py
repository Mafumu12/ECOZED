# Generated by Django 4.2.1 on 2023-08-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_alter_shipping_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_info',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]