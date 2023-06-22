from django.db import models

# Create your models here.
class detalhecurso (models.Model):
    
    cursoID = models.CharField(max_length=100)
    turmaID = models.CharField(max_length=100)
    