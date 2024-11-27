from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Tarea
from categorias.models import Categoria

# Create your views here.
@login_required
def create_tarea(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None

        Tarea.objects.create(titulo=titulo,descripcion=descripcion,categoria=categoria)
        return redirect('listar_tarea')
    return render(request,'create.html', {'categorias': categorias})

def listar_tareas(request):
    # Recoger los filtros de la URL (si existen)
    titulo = request.GET.get('titulo', '') # el segundo param es por si no lo encuentra no de error
    descripcion = request.GET.get('descripcion', '')
    categoria_id = request.GET.get('categoria', '')
    
    # trae todas las tareas
    tareas = Tarea.objects.select_related('categoria').all()

    # aplicar filtros
    if titulo:
        tareas = tareas.filter(titulo__icontains=titulo)  # filtro por titulo sin importar min/may
    if descripcion:
        tareas = tareas.filter(descripcion__icontains=descripcion)  # Filtro por descripcion, poco viable como filtro, ya que campo muy largo
    if categoria_id:
        tareas = tareas.filter(categoria__id=categoria_id)  # Filtro por categoria (suponiendo que categoria_id es un número)

    paginator = Paginator(tareas, 5)  # 5 tareas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener todas las categorías para el filtro de categoría
    categorias = Categoria.objects.all()

    return render(request, 'listar_tareas.html', {
        'page_obj': page_obj,
        'titulo': titulo,
        'descripcion': descripcion,
        'categoria_id': categoria_id,
        'categorias': categorias
    })

@login_required
def actualizar_tarea(request,id):
    #contexto={}
    tarea=get_object_or_404(Tarea,id=id)
    categorias = Categoria.objects.all()
    print(tarea.titulo)
    print(tarea.descripcion)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        tarea.categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None

        tarea.save()
        #contexto = {'tarea':tarea}
        return redirect('listar_tarea')
    return render(request,'actualizar_tarea.html',{'tarea':tarea, 'categorias': categorias})

@login_required
def eliminar_tarea(request, id):
    #contexto={}
    tarea=get_object_or_404(Tarea,id=id)
    if request.method == 'POST':
        tarea.delete()
        #contexto = {'tarea':tarea}
        return redirect('listar_tarea')
    return render(request,'eliminar_tarea.html',{'tarea':tarea})