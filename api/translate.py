from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

# Allow cross-origin requests (adjust allowed origins as needed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()

# Define a pydantic model for the translation request payload.
class TranslationRequest(BaseModel):
    name: str
    message: str
    target_language: str

# GET endpoint to handle translation via query parameters.
@app.get("/translate")
async def translate_get(message: str, language: str):
    try:
        translated = translator.translate(message, dest=language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        error_msg = f"Translation failed: {str(e)}"
        return JSONResponse(status_code=400, content={"error": error_msg})

# POST endpoint to handle translation via JSON payload.
@app.post("/translate")
async def translate_post(request: TranslationRequest):
    try:
        translated = translator.translate(request.message, dest=request.target_language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        error_msg = f"Translation failed: {str(e)}"
        return JSONResponse(status_code=400, content={"error": error_msg})
