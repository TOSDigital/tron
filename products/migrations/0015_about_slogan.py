# Generated by Django 4.2.4 on 2023-09-06 14:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_product_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='slogan',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]