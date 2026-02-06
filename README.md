# CRM API – Django REST Framework

API REST backend para la gestión de clientes (CRM simple), desarrollada con Django y Django REST Framework.
Proyecto orientado a demostrar buenas prácticas backend: autenticación real, seguridad básica, ownership de datos y despliegue en producción.

---

##  Stack Tecnológico
- Python 3.12
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (desarrollo) / PostgreSQL ready
- Git & GitHub
- Render (deploy)

---

##  Funcionalidades
- Registro de usuarios vía endpoint público
- Autenticación mediante JWT (access + refresh)
- CRUD completo de clientes
- Asociación automática de clientes al usuario autenticado
- Endpoint `/me` para obtener datos del usuario logueado
- Paginación personalizada
- Búsqueda y ordenamiento
- Rate limiting (throttling) para prevención de abusos
- Panel de administración Django

---

##  Seguridad
- Autenticación basada en JWT
- Endpoints protegidos por permisos
- Ownership por usuario (cada usuario accede solo a sus datos)
- Throttling para usuarios anónimos y autenticados

---

## Endpoints Principales

###  Autenticación
- `POST /api/auth/register/` → Registro de usuario
- `POST /api/auth/token/` → Login (JWT)
- `POST /api/auth/token/refresh/` → Refresh token
- `GET /api/auth/me/` → Usuario autenticado

###  Clientes (Protegidos)
- `GET /api/clients/` → Listar clientes
- `POST /api/clients/` → Crear cliente
- `GET /api/clients/{id}/` → Detalle cliente
- `PUT / PATCH /api/clients/{id}/` → Actualizar cliente
- `DELETE /api/clients/{id}/` → Eliminar cliente

---

##  Instalación Local

1. Clonar repositorio
2. Crear entorno virtual
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Configurar variables de entorno

5. Ejecutar migraciones:
    ```bash
    python manage.py migrate
    ```

6. Levantar servidor:
    ```bash
    python manage.py runserver
    ```

## Producción

API desplegada en Render:
https://crm-api-django.onrender.com/

Nota: los endpoints protegidos requieren token JWT válido.

## Testing
- Pruebas manuales realizadas con Insomnia
- Validación de endpoints públicos y protegidos por JWT

## Estado del Proyecto
- Funcional
- Autenticación real
- Desplegado en producción

## Posibles mejoras futuras
- Roles y permisos

- Dockerización

- Frontend

- Tests automatizados

## Autor
Diego Sade
Backend Developer – Python / Django