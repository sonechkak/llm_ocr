from fastapi import FastAPI, UploadFile, File

from src.apps.bot.api import bot_router
from src.apps.bot.services import summarizer
from src.core.settings import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    debug=settings.DEBUG
)

app.include_router(bot_router, prefix="/bot", tags=["bot"])


@app.post("/analyze-document")
async def analyze_document(file: UploadFile = File(...)):
    # 1. Сохранить файл временно
    # 2. Определить тип файла через file_detector
    # 3. Извлечь текст через соответствующий extractor
    # 4. Отправить в LLM
    # 5. Вернуть structured summary
    return summarizer.analyze_document(file)

