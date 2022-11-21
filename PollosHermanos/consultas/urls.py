from django.urls import path
from . import views


urlpatterns = [
    path('', views.consultas, name='consultas'),
    path('agregar/', views.agregar, name='agregar')
]
