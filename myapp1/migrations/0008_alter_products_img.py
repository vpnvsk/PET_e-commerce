# Generated by Django 4.1.5 on 2023-02-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0007_alter_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]