# Generated by Django 4.0.6 on 2022-10-16 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0001_initial'),
        ('tarea', '0002_alter_tarea_fecha_entrega_alter_tarea_hora_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_entrega',
            field=models.DateField(default='dd/mm/aaaa'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='hora_entrega',
            field=models.TimeField(default='hh:mm'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miembro.miembro'),
        ),
    ]
