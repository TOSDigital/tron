# Generated by Django 4.2.4 on 2023-09-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_rename_name_slug_team_tname_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_member_img',
            field=models.ImageField(default=1, upload_to='team/'),
            preserve_default=False,
        ),
    ]