# Generated by Django 4.1.5 on 2023-02-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0015_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp1.image'),
            preserve_default=False,
        ),
    ]
