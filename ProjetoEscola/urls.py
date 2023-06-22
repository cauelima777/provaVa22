"""ProjetoEscola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from rest_framework import routers
from aluno.views import alunoViewSet

rotas = routers.DefaultRouter() 

rotas.register(r'aluno',alunoViewSet, basename='aluno'),
rotas.register(r'Curso',alunoViewSet, basename='Curso'),
rotas.register(r'DetalheCurso',alunoViewSet, basename='DetalheCurso'),
rotas.register(r'DetalheDisciplina',alunoViewSet, basename='DetalheDisciplina'),
rotas.register(r'DetalheTurma',alunoViewSet, basename='DetalheTurma'),
rotas.register(r'Disciplina',alunoViewSet, basename='Disciplina'),
rotas.register(r'professor',alunoViewSet, basename='professor'),
rotas.register(r'ProjetoEscola',alunoViewSet, basename='ProjetoEscola'),
rotas.register(r'turma',alunoViewSet, basename='turma'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(rotas.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
