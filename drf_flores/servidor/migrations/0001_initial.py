# Generated by Django 2.2.6 on 2019-12-16 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='flor')),
                ('stock', models.IntegerField()),
                ('Estado', models.CharField(max_length=45, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servidor.Categoria')),
            ],
        ),
    ]
