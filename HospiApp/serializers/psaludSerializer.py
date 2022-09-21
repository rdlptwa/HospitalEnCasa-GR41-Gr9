from HospiApp.models.psalud import Personalsalud
from HospiApp.models.user import User
from rest_framework import serializers


class PersonalsaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud
        fields = ['username', 'rol', 'especialidad']