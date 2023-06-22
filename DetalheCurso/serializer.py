from rest_framework import serializers
from .models import detalhecurso

class detalhecursoSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = detalhecurso

        fields = '__all__'