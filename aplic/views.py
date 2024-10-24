from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm
from django.views.generic import TemplateView

class atualizarView(TemplateView):
    template_name = 'usuarios/atualizar_usuario.html'

class usuariosView(TemplateView):
    template_name = 'usuarios/criar_usuario.html'

class deletarView(TemplateView):
    template_name = 'usuarios/deletar_usuario.html'

class listarView(TemplateView):
    template_name = 'usuarios/listar_usuarios.html'

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/criar_usuario.html', {'form': form})

def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/atualizar_usuario.html', {'form': form})

def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})
