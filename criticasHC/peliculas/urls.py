from django.urls import path
from . import views 
urlpatterns=[
	path('',views.index,name='index'),
	path('criticas/',views.peliculas,name='pelis'),
	path('quienes/',views.quienes,name='quienes'),
	path('inicio/',views.inicio,name='inicio'),
	path('registro/',views.registro,name='registro'),
	path('movie/<str:pk>',views.MovieDetailView.as_view() ,name='movie_detail'),

	] 
urlpatterns +=[
	path('movie/create/',views.MovieCreate.as_view() ,name='movie_create'),
	path('movie/<str:pk>/update/',views.MovieUpdate.as_view() ,name='movie_update'),
	path('movie/<str:pk>/delete/',views.MovieDelete.as_view() ,name='movie_delete'),
	path('movie/<str:pk>/notas/',views.MovieNotas.as_view() ,name='movie_notas'),

]