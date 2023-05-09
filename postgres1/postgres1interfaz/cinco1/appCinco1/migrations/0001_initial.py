# Generated by Django 4.1.7 on 2023-05-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=30)),
                ('genero', models.TextField(max_length=30)),
                ('autor', models.TextField(max_length=30)),
                ('año', models.TextField(max_length=30)),
                ('trama', models.TextField(max_length=30)),
                ('espacio', models.TextField(max_length=30)),
                ('tiempo', models.TextField(max_length=30)),
                ('clasificacion', models.TextField(max_length=30)),
                ('editorial', models.TextField(max_length=30)),
                ('cantidadPags', models.IntegerField(default=0)),
            ],
        ),
    ]