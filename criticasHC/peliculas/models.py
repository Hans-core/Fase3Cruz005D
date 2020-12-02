from django.db import models
from django.urls import reverse 
import uuid
# Create your models here.
class Movie(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField (max_length=100)
	enum_gen =(
		('Accion','acc'),('Terror','terr'),('Horror','Horr'),('Comedia','Com'),('Ficción','fic'),('Otros','otro'),
		)
	gene = models.CharField (max_length=10, choices=enum_gen, blank=True, default='Otros')
	desc = models.TextField (max_length=1000, blank=True, default='')
	clasif = models.IntegerField ()
	clasifplu = models.IntegerField (blank = True, null = True)
	imagen = models.ImageField (upload_to='media/imagenes', null=True, blank=True, default='media/imagenes/not-found.png') 
	def get_absolute_url(self):
			return reverse ('movie_detail',args=[str(self.id)])	
	def __str__(self):
		return f'{self.name},{self.gene},{self.desc},{self.clasif}'

