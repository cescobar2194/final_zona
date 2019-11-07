from django.contrib.admin import widgets
from django import forms
from .models import Paciente, Medico, Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('paciente', 'medico', 'fecha',
        'hora', 'observaciones')

def __init__ (self, *args, **kwargs):
    super(CitaForm, self).__init__(*args, **kwargs)
    self.fields['fecha'].widget = forms.widgets.AdminSplitDateTime()
    self.fields['medico'].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields['medico'].help_text = "Seleccione un médico"
    self.fields['medico'].queryset = Medico.objects.all()
    self.fields['paciente'].widgets.CheckboxSelectMultiple()
    self.fields['paciente'].help_text = "Seleccione el paciente"
    self.fields['paciente'].queryset = Paciente.objects.all()

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido',
        'edad', 'sexo',)

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nombre', 'apellido',
        'especialidad', 'telefono',
        'fecha_nacimiento',)
