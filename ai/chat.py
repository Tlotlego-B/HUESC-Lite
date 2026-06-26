import requests
import json
import logging

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3"

def chat(prompt, model=DEFAULT_MODEL):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }, timeout=60)

        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No response from model.")
        else:
            logging.error(f"Ollama error {response.status_code}: {response.text}")
            return f"Ollama error {response.status_code}: {response.text}"
        
    except requests.exceptions.ConnectionError:
        return "Ollama is not running. Start it with: ollama serve"
    except requests.exceptions.Timeout:
        return "Ollama timed out. Try a shorter prompt or check your model."
    except Exception as e:
        logging.exception("Unexpected AI chat error")
        return f"AI chat error: {e}"
