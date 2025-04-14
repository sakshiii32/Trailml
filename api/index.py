from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()

# Define the request payload structure
class TranslationRequest(BaseModel):
    name: str
    message: str
    target_language: str

# POST endpoint for translation
@app.post("/translate")
async def translate_post(request: TranslationRequest):
    try:
        translated = translator.translate(request.message, dest=request.target_language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        error_msg = f"Translation failed: {str(e)}"
        return JSONResponse(status_code=400, content={"error": error_msg})