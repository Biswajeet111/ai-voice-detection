import base64
import io
from pydub import AudioSegment
import librosa

def decode_audio(base64_audio: str):
    audio_bytes = base64.b64decode(base64_audio)

    audio = AudioSegment.from_file(
        io.BytesIO(audio_bytes),
        format="mp3"
    )

    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)

    y, sr = librosa.load(wav_io, sr=None)
    return y, sr
