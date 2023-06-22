from django.shortcuts import render
from rest_framework import viewsets
from .models import Disciplina
from .serializer import DisciplinaSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated]