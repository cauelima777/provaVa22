from django.shortcuts import render
from rest_framework import viewsets
from .models import Professor
from .serializer import ProfessorSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticated]