# Generated by Django 4.1.5 on 2023-02-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='shoe_size',
            field=models.CharField(choices=[('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44')], max_length=5),
        ),
    ]
