# Generated by Django 5.1.3 on 2024-12-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrueba', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]