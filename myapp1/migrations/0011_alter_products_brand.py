# Generated by Django 4.1.5 on 2023-02-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0010_brand_alter_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(max_length=15),
        ),
    ]
