# Generated by Django 4.1.7 on 2023-03-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='short_dscription',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='product',
            name='marketing_price',
            field=models.FloatField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='marketing_price_promotional',
            field=models.FloatField(default=0, verbose_name='Promotional price'),
        ),
    ]