from django.db import models


# Create your models here.

class add(models.Model):
    
    nombre = models.CharField(max_length=80)
    image = models.ImageField()

    def __str__(self):
        return self.nombre