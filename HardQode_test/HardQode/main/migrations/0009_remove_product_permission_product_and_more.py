# Generated by Django 4.2.5 on 2023-09-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_permission_product_product_permission_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_permission',
            name='product',
        ),
        migrations.AddField(
            model_name='product_permission',
            name='product',
            field=models.ManyToManyField(to='main.product'),
        ),
    ]