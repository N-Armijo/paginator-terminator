# Norma Armijo

## **Practica Django**

Este proyecto es una practica en Django, que incluye funciones CRUD (Crear, Leer, Actualizar, Eliminar) y validaciones en el backend(pendientes). A continuación, encontrarás instrucciones detalladas para configurar el entorno y ejecutar el proyecto.

---

## **Configuración del Entorno Virtual**

### En Linux/Mac:
1. Crear el entorno virtual:
   ```bash
   python3 -m venv env
   ```
2. Activar el entorno virtual:
   ```bash
   source env/bin/activate
   ```

### En Windows CMD:
1. Crear el entorno virtual:
   ```cmd
   python -m venv env
   ```
2. Activar el entorno virtual:
   ```cmd
   env\Scripts\activate
   ```

### En Windows PowerShell:
1. Crear el entorno virtual:
   ```powershell
   python -m venv env
   ```
2. Activar permisos de ejecucion de scripts que viene desactivada por defecto. Cuidado con los parametros. En este caso el -Scope de ejecucion es solo proceso
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```
3. Activar el entorno virtual:
   ```powershell
   ./env/Scripts/activate
   ```

---

## **Instalación de Dependencias**

Asegúrate de tener un archivo **`requirements.txt`** en el proyecto con las dependencias necesarias.

1. Para instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Montar el Proyecto con Django**

### En Linux/Mac:
1. Ejecutar el servidor:
   ```bash
   python3 manage.py runserver
   ```

### En Windows CMD:
1. Ejecutar el servidor:
   ```cmd
   python manage.py runserver
   ```

### En Windows PowerShell:
1. Ejecutar el servidor:
   ```powershell
   python manage.py runserver
   ```

El proyecto estará disponible en `http://127.0.0.1:8000/`.

---

## **Pasos Generales para Usar la Aplicación**

1. Accede al proyecto en tu navegador en `http://127.0.0.1:8000/movies/`.
2. Funciones principales de la aplicación:
   - **Crear :** Completa el formulario y agrega una nueva .
   - **Listar :** Consulta todas las  disponibles en una tabla.
   - **Editar :** Haz clic en "Editar" para modificar la información de una  existente.
   - **Eliminar :** Haz clic en "Eliminar" y confirma para borrar una .
3. La aplicación valida los datos ingresados para garantizar que cumplan con las reglas especificadas.

---

## **Bajar el Servidor**

### En Linux/Mac o Windows (CMD/PowerShell):
Para detener el servidor, usa **CTRL+C** en la terminal donde está corriendo.

---
## **Desactivar el entorno virtual**

### En Linux/Mac o Windows (CMD/PowerShell):
```bash
deactivate
```
---
## **Notas Finales**
- Verificar que el entorno virtual esté activo antes de realizar cualquier operación, para evitar choque de versiones en el futuro.
- Si necesitas agregar más dependencias, actualiza el archivo **`requirements.txt`** ejecutando:
  ```bash
  pip freeze > requirements.txt
  ```
- En caso de dudas [documentación oficial de Django](https://docs.djangoproject.com/).

