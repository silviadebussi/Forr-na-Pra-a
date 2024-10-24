from django.contrib import admin
from django.urls import path, include
from aplic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplic.urls')),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/novo/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/editar/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
]
