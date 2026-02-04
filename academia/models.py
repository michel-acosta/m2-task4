from django.db import models
from django.contrib.auth.models import User

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.alumno.username} - {self.asignatura.nombre}"
