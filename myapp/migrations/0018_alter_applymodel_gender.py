# Generated by Django 4.2.5 on 2024-01-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_hired_by_hireermodel_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymodel',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
