from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from HospiApp import serializers

from HospiApp.serializers.psaludSerializer import PersonalsaludSerializer

class CrearPersonalsaludView(views.APIView):
    def post (self,request):
        serializers= PersonalsaludSerializer(data=request.data)
        if serializers.is_valid():
          serializers.save()
          return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)