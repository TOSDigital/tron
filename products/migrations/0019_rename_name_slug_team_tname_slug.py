# Generated by Django 4.2.4 on 2023-09-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_founder_fname_slug_team_name_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name_slug',
            new_name='tname_slug',
        ),
    ]