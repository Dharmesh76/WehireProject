# Generated by Django 4.2.5 on 2024-01-05 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_applymodel_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hireermodel',
            old_name='business_name',
            new_name='hired_by',
        ),
    ]
