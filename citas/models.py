from django.db import models
from django.contrib import admin

class Paciente(models.Model):
    nombre    = models.CharField(max_length=30)
    apellido  = models.CharField(max_length=20)
    edad      = models.IntegerField()
    sexo      = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Medico(models.Model):
    nombre           = models.CharField(max_length=30)
    apellido         = models.CharField(max_length=20)
    especialidad     = models.CharField(max_length=25)
    telefono         = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=12, blank=False, null=True)
    hora = models.CharField(max_length=6, blank=False, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

class CitaInLine(admin.TabularInline):
    model = Cita
    extra = 1

class MedicoAdmin(admin.ModelAdmin):
    inlines = (CitaInLine,)

class PacienteAdmin(admin.ModelAdmin):
    inlines = (CitaInLine,)

# Create your models here.
