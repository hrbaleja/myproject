# Generated by Django 4.1.3 on 2022-12-08 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0013_rename_list_a_ourservice_list_i_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourservice',
            old_name='listd_IV',
            new_name='list',
        ),
        migrations.RemoveField(
            model_name='ourservice',
            name='list_I',
        ),
        migrations.RemoveField(
            model_name='ourservice',
            name='list_II',
        ),
        migrations.RemoveField(
            model_name='ourservice',
            name='listc_III',
        ),
        migrations.RemoveField(
            model_name='ourservice',
            name='liste_V',
        ),
    ]