from django.shortcuts import render
from rest_framework import viewsets
from .models import detalhecurso
from .serializer import detalhecursoSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = detalhecurso.objects.all()
    serializer_class = detalhecursoSerializer
    permission_classes = [permissions.IsAuthenticated]