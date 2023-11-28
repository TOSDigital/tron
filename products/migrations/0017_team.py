# Generated by Django 4.2.4 on 2023-09-12 06:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_founder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member', models.CharField(max_length=200)),
                ('team_member_short', ckeditor_uploader.fields.RichTextUploadingField()),
                ('team_member_des', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]