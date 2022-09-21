from django.conf import settings
from rest_framework import generics, status
from HospiApp.models.paciente import Pacientes
from HospiApp.serializers.pacienteSerializer import PacienteSerializer
from rest_framework.response import Response

class ConsulPaciente(generics.ListAPIView):
    serializer_class = PacienteSerializer

    def get(self,request, pk, format=None):
        modelo = Pacientes.objects.get(pk=pk)
        serializer = PacienteSerializer(modelo)
        return Response(serializer.data)


