# Generated by Django 4.1.5 on 2023-06-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('si', models.IntegerField()),
                ('item', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
    ]
