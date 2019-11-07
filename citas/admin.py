from django.contrib import admin
from cita.models import Paciente, PacienteAdmin, Medico, MedicoAdmin, Cita, CitaInLine

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Cita)
# Register your models here.
