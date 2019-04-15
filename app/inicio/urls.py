from django.urls import path 

from . import views
from app.inicio.views import index , index2

urlpatterns = [
    path('index', views.index , name='index'),
    path('index2', views.index2.as_view() , name='index2'),

    
    
]
