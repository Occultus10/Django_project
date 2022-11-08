from django.db import models

# Create your models here.
class Curso(models.Model):
    fullname = models.CharField(max_length=50)
    edad = models.IntegerField()