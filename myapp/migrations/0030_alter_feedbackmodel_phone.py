# Generated by Django 4.2.5 on 2024-02-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_feedbackmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
