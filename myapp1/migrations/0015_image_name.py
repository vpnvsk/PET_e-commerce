# Generated by Django 4.1.5 on 2023-02-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0014_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
