# Generated by Django 4.2.5 on 2024-01-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_applymodel_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymodel',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]