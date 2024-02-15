from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100);
    apellidos = models.CharField(max_length=100);
    DNI = models.IntegerField();
    curso = models.CharField(max_length=100);
    nota = models.DecimalField(max_digits=5, decimal_places=2);