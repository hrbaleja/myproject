# Generated by Django 4.1.3 on 2022-11-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0004_alter_ourservice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservice',
            name='image',
            field=models.ImageField(blank=True, upload_to='Dataimage'),
        ),
    ]