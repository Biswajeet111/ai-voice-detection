from fastapi import FastAPI, Depends, HTTPException
from app.schemas import VoiceRequest, VoiceResponse
from app.auth import verify_api_key
from app.audio_utils import decode_audio
from app.detector import detect_voice

app = FastAPI(title="AI Voice Detection API")

SUPPORTED_LANGUAGES = [
    "Tamil",
    "English",
    "Hindi",
    "Malayalam",
    "Telugu"
]

@app.post("/api/voice-detection", response_model=VoiceResponse)
def voice_detection(
    request: VoiceRequest,
    api_key: str = Depends(verify_api_key)
):
    if request.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported language"
        )

    if request.audioFormat.lower() != "mp3":
        raise HTTPException(
            status_code=400,
            detail="Only mp3 audio format is supported"
        )

    y, sr = decode_audio(request.audioBase64)
    result = detect_voice(y, sr)

    return {
        "status": "success",
        "language": request.language,
        "classification": result["classification"],
        "confidenceScore": result["confidence"],
        "explanation": result["explanation"]
    }
