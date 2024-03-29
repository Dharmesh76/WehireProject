# Generated by Django 4.2.5 on 2024-01-08 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_applymodel_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiredModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('age', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('hired_by', models.TextField()),
            ],
        ),
    ]
