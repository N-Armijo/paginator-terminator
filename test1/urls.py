"""
URL configuration for test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views
from categorias import views as cat_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('crear_tarea', views.create_tarea, name='crear_tarea'),
    path('', views.listar_tareas, name='listar_tarea'),
    path('actualizar/<int:id>', views.actualizar_tarea, name='actualizar_tarea'),
    path('eliminar/<int:id>', views.eliminar_tarea, name='eliminar_tarea'),
    path('listar_categorias/', cat_views.listar_categorias, name='listar_categorias'),
    path('crear_categoria/', cat_views.crear_categoria, name='crear_categoria'),
    path('editar_categoria/<int:id>/', cat_views.editar_categoria, name='editar_categoria'),
    path('eliminar_categoria/<int:id>/', cat_views.eliminar_categoria, name='eliminar_categoria'),
]