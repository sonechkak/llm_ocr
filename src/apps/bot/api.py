from fastapi import APIRouter, Depends, FastAPI
from starlette import status


bot_router = APIRouter()

@bot_router.get("/status", status_code=status.HTTP_200_OK)
async def get_bot_status():
    """Check the status of the bot."""
    return {"status": "Bot is running"}
