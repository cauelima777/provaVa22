from django.db import models

# Create your models here.

class DetalheTurma (models.Model):
    
    alunoId = models.IntegerField()
    professorId = models.IntegerField()
    TurmaId = models.IntegerField()
    
    