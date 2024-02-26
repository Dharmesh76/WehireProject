# Generated by Django 4.2.5 on 2023-12-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hireerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('business_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=15)),
                ('zip', models.BigIntegerField()),
            ],
        ),
    ]