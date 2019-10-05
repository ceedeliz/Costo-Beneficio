from django.db import models

# Create your models here.
class Project(models.Model):
    @property
    def prueba(self):
        return "pruebapython"

    def pruebaint(self):
        return 10
