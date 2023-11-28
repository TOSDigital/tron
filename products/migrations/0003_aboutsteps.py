# Generated by Django 4.2.4 on 2023-08-23 14:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_about_mission_alter_about_vision_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Vision', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Mission', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('aboutsec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_steps', to='products.about')),
            ],
        ),
    ]
