# Generated by Django 4.1.6 on 2023-04-09 07:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(max_length=5000),
        ),
    ]
