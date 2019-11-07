# Generated by Django 2.2.7 on 2019-11-07 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=12, null=True)),
                ('hora', models.CharField(max_length=6, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=150, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.Paciente')),
            ],
        ),
    ]
