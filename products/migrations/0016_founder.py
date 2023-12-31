# Generated by Django 4.2.4 on 2023-09-08 05:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_about_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder_name', models.CharField(max_length=200)),
                ('founder_short_des', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('founder_des', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
