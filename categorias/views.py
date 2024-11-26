from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Categoria

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, 5)  # 5 tareas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listar_categorias.html', {'page_obj': page_obj})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('listar_tarea')
    return render(request, 'crear_categoria.html')

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'editar_categoria.html', {'categoria': categoria})

@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})
