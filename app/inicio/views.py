from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.

def index(request):
	return render(request, 'inicio/index.html')


class index2(TemplateView):
	template_name='inicio/index2.html'

