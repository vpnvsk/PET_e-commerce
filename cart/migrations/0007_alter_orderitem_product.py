# Generated by Django 4.2 on 2023-05-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsContent', '0007_productsize_size_delete_shoe_size_productsize_size_and_more'),
        ('cart', '0006_alter_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productsContent.products'),
        ),
    ]
