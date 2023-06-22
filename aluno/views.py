from django.shortcuts import render
from rest_framework import viewsets
from .models import aluno
from .serializer import alunoSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = aluno.objects.all()
    serializer_class = alunoSerializer
    permission_classes = [permissions.IsAuthenticated]