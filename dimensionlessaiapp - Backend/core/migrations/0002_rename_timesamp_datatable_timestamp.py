# Generated by Django 3.2.18 on 2023-04-10 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatable',
            old_name='timesamp',
            new_name='timestamp',
        ),
    ]
