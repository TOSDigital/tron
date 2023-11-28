# Generated by Django 4.2.4 on 2023-09-03 14:01

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_about_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('product_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('product_video', models.URLField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('p_video', models.URLField(blank=True, null=True)),
                ('product_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_product_image', to='products.product')),
            ],
        ),
    ]