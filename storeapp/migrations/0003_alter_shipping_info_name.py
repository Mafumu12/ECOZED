# Generated by Django 4.2.1 on 2023-08-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_shipping_info_email_shipping_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_info',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
