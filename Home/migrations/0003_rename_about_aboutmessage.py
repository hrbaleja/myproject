# Generated by Django 4.1.3 on 2022-12-06 06:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0002_about_delete_aboutus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Aboutmessage',
        ),
    ]