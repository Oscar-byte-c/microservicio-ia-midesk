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
└─ venv/
```
---
## ⚙️ Instalación y ejecución

### 1) Crear y activar entorno virtual

#### Windows (PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
