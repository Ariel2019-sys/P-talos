# Generated by Django 2.2.6 on 2019-10-30 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flor',
            name='estado',
        ),
    ]