from rest_framework import serializers
from .models import curso

class cursoSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = curso

        fields = '__all__'