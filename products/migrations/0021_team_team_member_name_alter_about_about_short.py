# Generated by Django 4.2.4 on 2023-10-02 09:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_team_team_member_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_member_name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_short',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
