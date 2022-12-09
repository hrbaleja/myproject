# Generated by Django 4.1.3 on 2022-12-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0011_revenue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourservice',
            old_name='lista',
            new_name='list_a',
        ),
        migrations.AlterField(
            model_name='revenue',
            name='Month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March ', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=256),
        ),
    ]
