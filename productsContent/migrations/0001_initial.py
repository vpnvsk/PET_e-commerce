# Generated by Django 4.1.5 on 2023-03-03 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('img1', models.ImageField(upload_to='image/%Y')),
                ('img2', models.ImageField(upload_to='image/%Y')),
                ('img3', models.ImageField(upload_to='image/%Y')),
            ],
        ),
        migrations.CreateModel(
            name='Shoe_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('f40', models.IntegerField()),
                ('f40d5', models.IntegerField()),
                ('f41', models.IntegerField()),
                ('f41d5', models.IntegerField()),
                ('f42', models.IntegerField()),
                ('f42d5', models.IntegerField()),
                ('f43', models.IntegerField()),
                ('f44', models.IntegerField()),
                ('f44d5', models.IntegerField()),
                ('f45', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='productsContent.brand')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsContent.image')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsContent.shoe_size')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
