# Generated by Django 4.1.3 on 2022-12-08 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0012_rename_lista_ourservice_list_a_alter_revenue_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourservice',
            old_name='list_a',
            new_name='list_I',
        ),
        migrations.RenameField(
            model_name='ourservice',
            old_name='listb',
            new_name='list_II',
        ),
        migrations.RenameField(
            model_name='ourservice',
            old_name='listc',
            new_name='listc_III',
        ),
        migrations.RenameField(
            model_name='ourservice',
            old_name='listd',
            new_name='listd_IV',
        ),
        migrations.RenameField(
            model_name='ourservice',
            old_name='liste',
            new_name='liste_V',
        ),
    ]