from django.shortcuts import render
from rest_framework import viewsets
from .models import DetalheTurma
from .serializer import DetalheTurmaSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer
    permission_classes = [permissions.IsAuthenticated]