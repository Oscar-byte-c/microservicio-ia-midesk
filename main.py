from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="Microservicio IA - MiDesk")

SYSTEM_PROMPT = """
Eres MiDesk, un asistente virtual del escritorio virtual "MiDesk".
Ayudas con uso del escritorio, tareas, notas y herramientas de estudio.
Si no es de MiDesk, responde: "Solo puedo ayudar con temas relacionados a MiDesk."
"""

class ChatRequest(BaseModel):
    mensaje: str

def contar_palabras(texto: str) -> int:
    # Conteo simple de "tokens" aproximados (palabras)
    return len(texto.strip().split()) if texto.strip() else 0

def respuesta_simulada_midesk(mensaje: str) -> str:
    m = mensaje.lower()

    if "tarea" in m or "organizo" in m or "pendiente" in m:
        return ("Para organizar tus tareas en MiDesk, crea listas por materia, "
                "asigna fechas límite y revisa tus pendientes diariamente.")

    if "nota" in m or "resumen" in m:
        return ("En MiDesk puedes crear notas por tema y organizarlas por fecha o materia "
                "para consultarlas rápidamente.")

    return "Solo puedo ayudar con temas relacionados a MiDesk."

@app.post("/chat")
def chat(req: ChatRequest):
    inicio = time.time()

    # Parámetros simulados (requisito académico)
    temperature = 0.3
    max_tokens = 300

    # Generar respuesta simulada
    respuesta = respuesta_simulada_midesk(req.mensaje)

    fin = time.time()
    tiempo_ms = int((fin - inicio) * 1000)

    # "Tokens" simulados como palabras
    tokens_entrada = contar_palabras(req.mensaje)
    tokens_salida = contar_palabras(respuesta)
    tokens_totales = tokens_entrada + tokens_salida

    # Mostrar métricas en consola (opcional, pero útil para evidencia)
    print(f"[MÉTRICAS] tiempo_ms={tiempo_ms} | entrada={tokens_entrada} | salida={tokens_salida} | total={tokens_totales}")

    # Devolver métricas en JSON
    return {
        "respuesta": respuesta,
        "modo": "simulado (proyecto académico)",
        "parametros_modelo": {
            "temperature": temperature,
            "max_tokens": max_tokens
        },
        "metricas": {
            "tiempo_respuesta_ms": tiempo_ms,
            "tokens_entrada_aprox": tokens_entrada,
            "tokens_salida_aprox": tokens_salida,
            "tokens_totales_aprox": tokens_totales
        }
    }
