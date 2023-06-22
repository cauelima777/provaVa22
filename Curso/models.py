from django.db import models

# Create your models here.

class curso (models.Model):
    
    codigo = models.IntegerField()
    nome = models.CharField(max_length=100)
    