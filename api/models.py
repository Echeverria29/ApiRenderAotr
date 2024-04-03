from django.db import models

# Create your models here.
class Datos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
      return self.nombre
  

    class Meta:
       
        db_table = 'datos'