# Generated by Django 2.2.6 on 2019-10-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreria', '0002_remove_flor_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='Estado',
            field=models.TextField(null=True),
        ),
    ]
