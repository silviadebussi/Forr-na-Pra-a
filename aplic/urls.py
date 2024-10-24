from django.urls import path
from django.http import HttpResponseRedirect
from aplic.views import listar_usuarios, criar_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/usuarios/')),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/criar/', criar_usuario, name='criar_usuario'),
    path('usuarios/atualizar/<int:id>/', atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/deletar/<int:id>/', deletar_usuario, name='deletar_usuario'),
]
