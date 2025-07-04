import requests


class LlmService:
    """Сервис для ламы."""

    def __init__(self, model="llama3.2"):
        self.model = model
        self.base_url = "http://localhost:11434"

    def call_ollama(self, prompt):
        url = f"{self.base_url}/api/generate"
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "max_tokens": 2048,
            "temperature": 0.3,
        }
        try:
            response = requests.post(url, json=data, timeout=120)
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response.json()["response"]

        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка вызова Ollama API: {str(e)}")
