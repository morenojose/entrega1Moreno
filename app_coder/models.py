from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    

class Alumno(models.Model):
    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad=models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()
