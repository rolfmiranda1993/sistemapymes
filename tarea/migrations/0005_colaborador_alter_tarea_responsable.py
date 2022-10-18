# Generated by Django 4.0.6 on 2022-10-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0004_tareamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tarea.colaborador'),
        ),
    ]
