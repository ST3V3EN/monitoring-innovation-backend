# Monitoring Innovation Backend

Este proyecto es un backend desarrollado como parte de una prueba técnica para la empresa Monitoring Innovation (AB COMERCIAL). El objetivo principal es gestionar información relacionada con vehículos, proporcionando una API robusta y escalable.

## Tabla de Contenidos
- [Descripción General](#descripción-general)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Endpoints Principales](#endpoints-principales)
- [Colección Postman](#colección-postman)
- [Autores](#autores)

## Descripción General
Este backend está diseñado para gestionar operaciones CRUD sobre entidades relacionadas con vehículos. Permite la creación, consulta, actualización y eliminación de registros, así como la integración con bases de datos y la documentación de endpoints para pruebas y desarrollo.

## Tecnologías Utilizadas
- *Python 3.11+*
- *FastAPI*: Framework principal para la creación de la API REST.
- *SQLAlchemy*: ORM para la gestión de la base de datos.
- *Uvicorn*: Servidor ASGI para desarrollo y producción.
- *Pydantic*: Validación y serialización de datos.
- *Postman*: Para pruebas de endpoints (colección incluida).


## Instalación
1. Clona el repositorio:
   bash
   git clone <URL-del-repositorio>
   cd monitoring-innovation-backend
   
2. Crea un entorno virtual e instala las dependencias:
   bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   

## Ejecución
1. Inicia el servidor de desarrollo:
   bash
   uvicorn app.main:app --reload
   
2. Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints Principales
- *GET /cars*: Listar todos los vehículos
- *POST /cars*: Crear un nuevo vehículo
- *GET /cars/{id}*: Obtener detalles de un vehículo
- *PUT /cars/{id}*: Actualizar información de un vehículo
- *DELETE /cars/{id}*: Eliminar un vehículo

> Nota: Puedes consultar la colección de Postman incluida en app/collections/Monitoring Innovation.postman_collection.json para probar todos los endpoints fácilmente.

## Colección Postman
La colección de Postman contiene ejemplos de peticiones para todos los endpoints implementados. Importa el archivo en Postman para comenzar a probar la API rápidamente.

## Autores
- Desarrollador: Brayan Steven Moreno Garcia
- Empresa: Monitoring Innovation (AB COMERCIAL)

---
Este proyecto fue desarrollado como parte de una prueba técnica y puede ser extendido o adaptado según los requerimientos de la empresa.
