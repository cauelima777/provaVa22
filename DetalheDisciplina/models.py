from django.db import models

# Create your models here.
class DetalheDisciplina (models.Model):
    
    curso = models.IntegerField()
    disciplina = models.IntegerField()