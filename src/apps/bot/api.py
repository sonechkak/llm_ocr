from fastapi import APIRouter, Depends, FastAPI, File, UploadFile, HTTPException
from starlette import status

from .services.summarizer import summarize_document

bot_router = APIRouter()

@bot_router.post("/summarize", status_code=status.HTTP_201_CREATED)
async def bot_result(file: UploadFile = File(...)):
    """Summarizes the uploaded document."""
    try:
        summary = await summarize_document(file)
        return {
            "summary": summary,
            "filename": file.filename,
        }
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=str(e)
        )
