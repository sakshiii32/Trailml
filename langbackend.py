from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from googletrans import Translator

# Create FastAPI instance
app = FastAPI()

# Configure CORS middleware to allow cross-origin requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of the Translator
translator = Translator()

# Define the Pydantic model for POST translation requests
class TranslationRequest(BaseModel):
    name: str
    message: str
    target_language: str

# GET endpoint to handle translation via query parameters
@app.get("/translate")
async def translate_get(message: str, language: str):
    try:
        # Await the asynchronous translate method
        translated = await translator.translate(message, dest=language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        error_msg = f"Translation failed: {str(e)}"
        return JSONResponse(status_code=400, content={"error": error_msg})

# POST endpoint to handle translation via JSON payload
@app.post("/translate")
async def translate_post(request: TranslationRequest):
    try:
        # Await the asynchronous translate method
        translated = await translator.translate(request.message, dest=request.target_language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        error_msg = f"Translation failed: {str(e)}"
        return JSONResponse(status_code=400, content={"error": error_msg})

# To run the server, execute:
# uvicorn langbackend:app --reload

