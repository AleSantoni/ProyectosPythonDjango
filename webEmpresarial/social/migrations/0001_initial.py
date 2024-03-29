# Generated by Django 5.0 on 2024-01-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.SlugField(max_length=100, unique=True, verbose_name='Nombre Clave')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Emlace')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
                'ordering': ['name'],
            },
        ),
    ]
