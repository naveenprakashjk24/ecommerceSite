# Generated by Django 4.0.1 on 2022-01-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
