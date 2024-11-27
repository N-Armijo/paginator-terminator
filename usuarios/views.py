from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Cuenta creada para {username}!")
            return redirect('iniciar_sesion')
        else:
            messages.error(request, 'Hubo un error al crear tu cuenta. Intenta de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})
    # return render(request, 'usuarios/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido de nuevo, {username}!')
                return redirect('listar_tarea')  # Redirige a la lista de tareas o a la página principal
            else:
                messages.error(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Formulario inválido')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
    # return render(request, 'usuarios/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente')
    return redirect('iniciar_sesion')