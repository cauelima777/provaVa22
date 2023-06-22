from django.shortcuts import render
from rest_framework import viewsets
from .models import DetalheDisciplina
from .serializer import DetalheDisciplinaSerializer
from rest_framework import permissions
# Create your views here.


class alunoViewSet(viewsets.ModelViewSet): 

    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated]