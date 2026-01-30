# Microservicio IA - MiDesk 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20REST-success)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-informational)
![Status](https://img.shields.io/badge/Status-Proyecto%20Acad%C3%A9mico-yellow)

Microservicio en **Python + FastAPI** que expone un endpoint REST para un asistente tipo **MiDesk**.  
El objetivo es demostrar: **API REST, prompt (System Role), parámetros y métricas**.

---

## ✨ Características
- Endpoint **POST `/chat`** que recibe y devuelve **JSON**
- **System Prompt** (rol del asistente) para mantener el contexto MiDesk
- Parámetros de generación (ej. `temperature`, `max_tokens`)
- Métricas básicas (ej. **tiempo de respuesta** y/o conteo aproximado de tokens/palabras)
- Documentación automática con Swagger: **`/docs`**

---

## 🧰 Tecnologías
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- (Opcional) **python-dotenv** para variables de entorno

---

## 📁 Estructura del proyecto (ejemplo)
```txt
microservicio-ia-python/
├─ main.py
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ venv/                  (no se sube a GitHub)
⚙️ Instalación y ejecución
1) Crear y activar entorno virtual
Windows (PowerShell):

python -m venv venv
venv\Scripts\activate
Linux/macOS:

python -m venv venv
source venv/bin/activate
2) Instalar dependencias
pip install -r requirements.txt
3) Ejecutar el servidor
uvicorn main:app --reload
4) Abrir documentación (Swagger)
http://127.0.0.1:8000/docs

🔌 Uso del API
Endpoint
POST /chat

Request (JSON)
{
  "mensaje": "¿Cómo organizo mis tareas en MiDesk?"
}
Response (JSON) — ejemplo
{
  "respuesta": "Para organizar tus tareas en MiDesk, crea listas por materia...",
  "parametros_modelo": {
    "temperature": 0.3,
    "max_tokens": 300
  },
  "metricas": {
    "tiempo_respuesta_ms": 12,
    "tokens_totales_aprox": 28
  }
}
🧪 Pruebas rápidas (Postman)
Método: POST

URL: http://127.0.0.1:8000/chat

Header: Content-Type: application/json

Body (raw → JSON):

{ "mensaje": "Hola MiDesk" }
🔒 Seguridad (importante)
Nunca subas archivos con claves (.env) al repositorio.

Asegúrate de incluir en .gitignore:

venv/
.env
__pycache__/
