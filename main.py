from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time
from google import genai

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="Microservicio IA - MiDesk (Google Gemini)")

SYSTEM_PROMPT = """
Eres MiDesk, un asistente virtual del escritorio MiDesk.
Ayudas con organización académica, tareas y notas.
Si la pregunta NO es sobre MiDesk responde:
"Solo puedo ayudar con temas relacionados a MiDesk."
"""

class ChatRequest(BaseModel):
    mensaje: str

@app.post("/chat")
def chat(req: ChatRequest):
    inicio = time.time()
    temperature = 0.3
    max_tokens = 300

    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return {"error": "GOOGLE_API_KEY no encontrada en .env"}

        client = genai.Client(api_key=api_key)

        prompt = f"{SYSTEM_PROMPT}\nUsuario: {req.mensaje}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        fin = time.time()

        return {
            "respuesta": response.text,
            "parametros_modelo": {
                "temperature": temperature,
                "max_tokens": max_tokens
            },
            "metricas": {
                "tiempo_respuesta_ms": int((fin - inicio) * 1000)
            }
        }

    except Exception as e:
        return {
            "error": "Fallo al generar respuesta",
            "detalle": str(e)
        }
