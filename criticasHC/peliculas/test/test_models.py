from django.test import TestCase,Client
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

class ViewTest(TestCase):
	def test_peliculas(self):
		c= Client()
		resp=c.get('/peliculas/')
		self.assertEqual(resp.status_code, 200)
	def test_criticas(self):
		o= Client()
		resp=o.get('/peliculas/criticas/')
		self.assertEqual(resp.status_code, 200)
	def test_quienes(self):
		co= Client()
		resp=co.get('/peliculas/quienes/')
		self.assertEqual(resp.status_code, 200)
	def test_InicioSesion(self):
		i= Client()
		resp=i.get('/accounts/login/')
		self.assertEqual(resp.status_code, 200)

