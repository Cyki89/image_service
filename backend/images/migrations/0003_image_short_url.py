# Generated by Django 4.0.3 on 2022-08-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_expires_link_accounttier_allow_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='short_url',
            field=models.URLField(null=True),
        ),
    ]