# Generated by Django 4.2.5 on 2023-12-25 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_hireermodel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='jobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
                ('salary', models.TextField()),
                ('location', models.TextField()),
                ('job_description', models.TextField()),
                ('added_by', models.TextField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.catagory_list')),
            ],
        ),
    ]
