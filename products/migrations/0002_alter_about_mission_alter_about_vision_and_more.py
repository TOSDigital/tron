# Generated by Django 4.2.4 on 2023-08-23 14:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Mission',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='Vision',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
