# Generated by Django 4.0.3 on 2022-07-20 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttier',
            old_name='expires_link',
            new_name='allow_download',
        ),
    ]
