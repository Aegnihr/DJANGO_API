# Generated by Django 4.2.10 on 2024-02-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('DNI', models.IntegerField()),
                ('curso', models.CharField(max_length=100)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
