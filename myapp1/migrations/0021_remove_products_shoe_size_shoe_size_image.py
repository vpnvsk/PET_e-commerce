# Generated by Django 4.1.5 on 2023-02-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0020_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='shoe_size',
        ),
        migrations.CreateModel(
            name='Shoe_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_40', models.IntegerField()),
                ('_40_5', models.IntegerField()),
                ('_41', models.IntegerField()),
                ('_41_5', models.IntegerField()),
                ('_42', models.IntegerField()),
                ('_42_5', models.IntegerField()),
                ('_43', models.IntegerField()),
                ('_44', models.IntegerField()),
                ('_44_5', models.IntegerField()),
                ('_45', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='myapp1.products')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='image/%Y')),
                ('img2', models.ImageField(upload_to='image/%Y')),
                ('img3', models.ImageField(upload_to='image/%Y')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp1.products')),
            ],
        ),
    ]