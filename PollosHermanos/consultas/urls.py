from django.urls import path
from . import views


urlpatterns = [
    path('', views.consultas, name='consultas'),

    # urls agregar
    path('agregarProv/', views.agregarProv, name='agregarProv'),
    path('agregarProd/', views.agregarProd, name='agregarProd'),
    path('agregarSuc/', views.agregarSuc, name='agregarSuc'),
    path('agregarComb/', views.agregarComb, name='agregarComb'),

    # urls eliminar
    path("eliminarProv/<int:tbProveedores_id>/", views.eliminarProv, name='eliminarProv'),
    path("eliminarProd/<int:tbProductos_id>/", views.eliminarProd, name='eliminarProd'),
    path("eliminarSuc/<int:tbSucursales_id>/", views.eliminarSuc, name = 'eliminarSuc'),
    path("eliminarComb/<int:tbCombos_id>/", views.eliminarComb, name = 'eliminarComb'),
    
    # urls editar
    path("editarProv/<int:tbProveedores_id>/", views.editarProv, name='editarProv'),
    path("editarProd/<int:tbProductos_id>/", views.editarProd, name='editarProd'),
    path("editarSuc/<int:tbSucursales_id>/", views.editarSuc, name='editarSuc'),
    path("editarComb/<int:tbCombos_id>/", views.editarComb, name='editarComb'),
]
