from django.db import models
from .user import User
from .psalud import Personalsalud

class Pacientes (models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_psalud = models.ForeignKey(Personalsalud,related_name='paciente', on_delete=models.CASCADE)
    username= models.ForeignKey(User,related_name='paciente', on_delete=models.CASCADE)
    cyty = models.CharField('Ciudad',max_length=15)
    birthday = models.DateField('fecha de nacimiento')