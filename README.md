<h1>Proyecto_Arkandha</h1>

Este proyecto es una aplicación web desarrollada con Django para la administración de predios (propiedades) y sus propietarios. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre predios y propietarios, y gestionar la relación entre ellos.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Contacto](#contacto)

## Características

- **Gestión de Predios:**
  - Listar todos los predios registrados.
  - Crear, editar y eliminar predios.
  - Asociar uno o varios propietarios a cada predio.
  - Validación de datos únicos (por ejemplo, número catastral y matrícula).

- **Gestión de Propietarios:**
  - Listar todos los propietarios.
  - Crear, editar y eliminar propietarios.
  - Visualizar los predios asociados a cada propietario.

- **Interfaz de Usuario:**
  - Diseño responsivo y moderno utilizando [Bootstrap](https://getbootstrap.com/).
  - Formularios con validaciones en el lado del cliente (HTML5) y en el servidor (Django).
  - Mensajes de error y confirmaciones para acciones críticas (eliminación de registros).

## Tecnologías

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Base de Datos:** PostgreSQL

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Cristopher1178Col/arkandha.git
   cd arkandha
2. **Crear y activar el entorno virtual**
   ```bash
   python -m venv env
   source env/bin/activate
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt 
   pip list --- verificas que esten las dependencias instaladas.
4. **Configurar la aplicacion y la base de datos**
    - [Configuración](#configuración)
5. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver

## Configuración
1. **Crear la base de datos**
     1. Abrir PostgreSQL en tu terminal o en tu herramienta de gestion
     2. Ejecutar el siguiente comando para crear la base de datos
        ```sql
           CREATE DATABASE arkandha;
  
     3. Crear un usuario y asignar permisos:
         ```sql
           CREATE USER 'tu_user' WITH PASSWORD 'tu_password'; ------ Debes crear tu usuario y contraseña entre comillas simples ('')
           ALTER DATABASE arkandha OWNER TO 'user';

2. **Configurar conexion a Django**
     1. Abrir el archivo `settings.py` en la carpeta arkandha
     2. Buscar la seccion `DATABASES` y verificar que este la base de datos creada (arkandha)
        Deberia aparecer asi:
        ```py
        DATABASES = {
         'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'arkandha',         # Nombre de la db que se creo en PostgreSQL
           'USER': 'tu_user',    # Usuario de PostgreSQL
           'PASSWORD': 'tu_password',
           'HOST': 'localhost',
           'PORT': '5432',
          }
        }

3. **Aplicar migraciones**
     Ejecutar los siguientes comandos para aplicar las migraciones y asegurarte de que la base de datos esta lista
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
     Si todo esta correcto deberia correr la aplicacion en tu servidor local 
  

## Uso
**Home:**
- Accede a http://localhost:8000/home/ para ver los modulos de predios y propietarios

**Predios:**
- Accede a http://localhost:8000/predios/ para ver la lista de predios, y desde allí podrás crear, editar o eliminar un predio.

**Propietarios:**
- Accede a http://localhost:8000/propietarios/ para ver la lista de propietarios, crear nuevos, editar o eliminar registros, y ver los predios asociados a cada propietario.

## Contacto
- **Nombre: Cristopher Benavides**
- **Email: benavidesramirez316@gmail.com**
- **GitHub: Cristopher1178Col**
