import os
import tempfile

from fastapi import File

from ..services.extract_text import extract_text_from_file
from ..services.llm_service import LlmService


async def summarize_document(file: File):
    """Summarizes the given text using an LLM."""
    # Сохраняем файл временно
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        content = await file.read()
        tmp_file.write(content)
        tmp_file_path = tmp_file.name

    try:
        # Извлекаем текст в зависимости от типа файла
        text = extract_text_from_file(tmp_file_path, file.content_type)

        if not text.strip():
            return "Не удалось извлечь текст из файла"

        prompt = f"""
            Проанализируй этот документ и дай краткое резюме:
            - Тип документа
            - Основные моменты (3-5 пунктов)  
            - Ключевые данные/цифры если есть
            - Цель документа
            - Целевая аудитория
            - Важные выводы

            Текст документа:
            {text[:3000]}  # Ограничиваем длину
            """

        llm_service = LlmService("llama3.2")
        summary = llm_service.call_ollama(prompt)
        return summary

    finally:
        # Удаляем временный файл
        os.unlink(tmp_file_path)
