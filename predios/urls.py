# predios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Predios
    path('predios/', views.listar_predios, name='listar_predios'),
    path('predios/crear/', views.crear_predio, name='crear_predio'),
    path('predios/editar/<int:pk>/', views.editar_predio, name='editar_predio'),
    path('predios/eliminar/<int:pk>/', views.eliminar_predio, name='eliminar_predio'),
    path('propietario/<int:pk>/predios/', views.predios_propietario, name='predios_propietario'),


    # Propietarios
    path('predio/<int:pk>/propietarios/', views.listar_propietarios, name='listar_propietarios'),  # Lista propietarios de un predio específico
    path('propietarios/', views.listar_todos_propietarios, name='listar_todos_propietarios'),  # Lista TODOS los propietarios
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:pk>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:pk>/', views.eliminar_propietario, name='eliminar_propietario'),
    path('predios/<int:pk>/propietario/', views.propietario_predio, name='propietario_predio'),

    # Página de inicio
    path('home/', views.home, name='home'),
]
