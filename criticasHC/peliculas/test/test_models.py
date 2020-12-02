from django.test import TestCase
from peliculas.models import Movie 
class PruebaM(TestCase):
	@classmethod


	def setUpTestData(cls):
		Movie.objects.create(id='7c32217e-7347-4bf5-82d7-3f71d48d2ad7',name='nombre', gene='Accion', desc='hola', clasif=2 ,)
	
	def test_name_label(self):
		movie=Movie.objects.get(id='7c32217e-7347-4bf5-82d7-3f71d48d2ad7')
		field_label = Movie._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')

	def test_gene_label(self):
		movie=Movie.objects.get(id='7c32217e-7347-4bf5-82d7-3f71d48d2ad7')
		field_label = Movie._meta.get_field('gene').verbose_name
		self.assertEquals(field_label,'gene')

	def test_desc_label(self):
		movie=Movie.objects.get(id='7c32217e-7347-4bf5-82d7-3f71d48d2ad7')
		field_label = Movie._meta.get_field('desc').verbose_name
		self.assertEquals(field_label,'desc')

	def test_clasif_label(self):
		movie=Movie.objects.get(id='7c32217e-7347-4bf5-82d7-3f71d48d2ad7')
		field_label = Movie._meta.get_field('clasif').verbose_name
		self.assertEquals(field_label,'clasif')

