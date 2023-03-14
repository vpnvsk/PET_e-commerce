# Generated by Django 4.1.5 on 2023-03-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsContent', '0006_remove_products_size_shoe_size_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsContent.products')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Shoe_size',
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsContent.size'),
        ),
        migrations.AddField(
            model_name='products',
            name='sizes',
            field=models.ManyToManyField(through='productsContent.ProductSize', to='productsContent.size'),
        ),
    ]
