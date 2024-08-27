from django.db import models
from .choices import generos

#modelo docente:
class Docente(models.Model):
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    genero = models.CharField(max_length=1, choices=generos, default='F')

    def nombre_completo(self):
        return "{} , {}".format(self.apellido, self.nombres)
    #nombre completo del docente:
    def __str__(self):
        return self.nombre_completo()
    
    #para personalizar el nombre con el cual se crea la tabla
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering = ['apellido']


#modelo para postgreSQL universidad
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(
        Docente, null=True, blank=True, on_delete=models.CASCADE) #crea clave foranea para relacionar Curso con Docente

    #para que muestre el nombre en el panel de adminsitracion y no el id:
    def __str__(self):
        return self.nombre
    
 


    

