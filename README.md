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
   pip install "dependencia"  -------- las dependencias estan en el archivo requirements.txt de este repositorio
   pip list --- verificas que esten las dependencias instaladas.
4. **Realizar migraciones de la base de datos**
    ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver

## Configuración
- Revisa la configuración de DATABASES para conectar con PostgreSQL.

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
