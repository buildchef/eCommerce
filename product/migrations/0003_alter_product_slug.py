# Generated by Django 4.1.7 on 2023-02-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
