from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.
class Categoria(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    calificacion=models.IntegerField()

    def __str__(self):
        return self.name

class Flor(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    valor=models.IntegerField()
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='flor',null=True)
    stock=models.IntegerField()
    Estado=models.CharField(max_length=45,null=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    usuario=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    total=models.IntegerField()
    fecha=models.DateField()

    def __str__(self):
        return str(self.usuario)+''+str(self.nombre)

class Meta:
    permission =(
        ('Cliente',_('el Cliente')),
    )   
