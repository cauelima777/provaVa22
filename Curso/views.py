from django.shortcuts import render
from rest_framework import viewsets
from .models import curso
from .serializer import cursoSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = curso.objects.all()
    serializer_class = cursoSerializer
    permission_classes = [permissions.IsAuthenticated]