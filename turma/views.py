from django.shortcuts import render
from rest_framework import viewsets
from .models import Turma
from .serializer import TurmaSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [permissions.IsAuthenticated]