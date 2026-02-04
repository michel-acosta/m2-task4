# Servidor de Notas Académicas - Django

Servidor desarrollado con Django y Django REST Framework para la gestión de asignaturas y notas académicas.

## Funcionalidades
- Gestión de usuarios con roles (Profesores / Alumnos)
- CRUD de asignaturas
- CRUD de notas
- Control de permisos por rol
- API REST con autenticación por token
- Base de datos MySQL / MariaDB

## Instalación
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
