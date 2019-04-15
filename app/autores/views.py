from django.shortcuts import render
from django.views import generic
from app.autores.models import Autor
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,  CreateView , ListView
# Create your views here.

class registrarautores(CreateView):
	template_name='autores/regitrarautor.html'
	model=Autor
	fields=['nombre',
			'pais',
			'descripcion',
			
			'foto',
			]
	success_url= reverse_lazy('mostrar')

class mostrar(ListView):
	template_name='autores/reportar.html'
	model= Autor
