import requests


class LlmService:
    """Service for interacting with LLM models via Ollama API."""

    def __init__(self, model="llama3.2"):
        self.model = model
        self.base_url = f"http://localhost:11434"

    def call_ollama(self, prompt):
        url = f"{self.base_url}/api/generate"
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "max_tokens": 1000,
            "temperature": 0.7
        }
        try:
            response = requests.post(url, json=data, timeout=120)
            response.raise_for_status()
            return response.json()["response"]

        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка вызова Ollama API: {str(e)}")
