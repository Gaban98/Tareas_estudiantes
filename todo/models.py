from django.db import models

# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)
    def __str__(self):
        return self.tarea