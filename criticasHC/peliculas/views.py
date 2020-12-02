from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
	return render(request, 'index.html')
def peliculas(request):
	numpeli = Movie.objects.all() 
	return render(request, 'pelis.html', context={"numpeli":numpeli} )
def quienes(request):
	return render(request, 'quienes.html')
def inicio(request):
	return render(request, 'inicio.html')
def registro(request):
	return render(request, 'registro.html')
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class MovieCreate(CreateView):
    model = Movie
    fields ='__all__' 

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name','gene','clasif','desc','imagen',]

class MovieNotas(UpdateView):
    model = Movie
    fields = ['clasifplu',]

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('pelis')

from django.views import generic

class MovieDetailView(generic.DetailView):
    model = Movie

