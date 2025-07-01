from fastapi import FastAPI, UploadFile, File

from src.apps.bot.api import bot_router
from src.core.settings import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    debug=settings.DEBUG
)

app.include_router(bot_router, prefix="/bot", tags=["bot"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Bot API"}