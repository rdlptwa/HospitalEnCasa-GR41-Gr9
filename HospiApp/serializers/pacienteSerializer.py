from HospiApp.models.paciente import Pacientes
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ['psalud_id','username','city','birthday']