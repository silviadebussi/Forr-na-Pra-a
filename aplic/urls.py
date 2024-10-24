from django.contrib import admin
from django.urls import path
from .views import listar_usuarios, criar_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('novo/', criar_usuario, name='criar_usuario'),
    path('editar/<int:id>/', atualizar_usuario, name='atualizar_usuario.html'),
    path('deletar/<int:id>/', deletar_usuario, name='deletar_usuario'),
]