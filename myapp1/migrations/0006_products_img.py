# Generated by Django 4.1.5 on 2023-02-12 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]
