# Generated by Django 4.1.7 on 2023-03-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.EmailField(blank=True, max_length=150, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('time', models.TimeField()),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
