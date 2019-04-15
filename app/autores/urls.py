from django.urls import path 

from . import views
from app.autores.views import registrarautores , mostrar

urlpatterns = [
    path('registro', views.registrarautores.as_view() , name='registro'),
    path('mostrar', views.mostrar.as_view() , name='mostrar'),


    ]