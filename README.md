# 🎤 AI-Generated Voice Detection API

A secure REST API that detects whether a given voice sample is **AI-generated** or **spoken by a real human**.  
The system supports **five Indian languages** and is designed for accuracy, reliability, and explainability.

---

## 🚀 Problem Statement

With the rise of AI voice cloning and text-to-speech systems, it has become increasingly difficult to distinguish between real human voices and synthetic AI-generated voices.

This project solves that problem by analyzing audio characteristics and classifying a voice as:

- **AI_GENERATED**
- **HUMAN**

---

## 🌍 Supported Languages

The API strictly supports the following languages:

- Tamil
- English
- Hindi
- Malayalam
- Telugu

Each request must contain **one audio file in exactly one of these languages**.

---

## 🧠 Approach & Methodology

The system uses **audio signal processing and machine learning–oriented heuristics** to detect synthetic speech patterns.

### Key audio characteristics analyzed:
- **MFCC (Mel Frequency Cepstral Coefficients)** – spectral features
- **Pitch stability (F0)** – AI voices often show unnaturally stable pitch
- **Energy variation** – human speech has natural fluctuations
- **Overall feature variability**

### Why this works:
- AI-generated voices are usually **over-smoothed**
- Human voices contain **micro-variations** due to emotion, breath, and articulation
- These patterns are **language-independent**, making the solution robust across all 5 languages

---

## 🔐 API Security

All API requests are protected using an **API Key**.

### Required Header
x-api-key: YOUR_SECRET_API_KEY

yaml
Copy code

Requests without a valid API key are rejected.

---

## 📡 API Endpoint

### POST `/api/voice-detection`

---

## 📥 Request Format

### Headers
```http
Content-Type: application/json
x-api-key: sk_test_123456789
Body
json
Copy code
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "BASE64_ENCODED_MP3_AUDIO"
}
Request Rules
Audio format must be MP3

Audio must be Base64 encoded

Only one audio file per request

Audio must not be modified

📤 Response Format (Success)
json
Copy code
{
  "status": "success",
  "language": "Tamil",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.86,
  "explanation": "Unnatural pitch stability and low vocal variability detected"
}
Response Fields
Field	Description
status	success / error
language	Detected language
classification	AI_GENERATED or HUMAN
confidenceScore	Confidence value between 0.0 and 1.0
explanation	Short reasoning behind the decision

❌ Error Response Example
json
Copy code
{
  "status": "error",
  "message": "Invalid API key or malformed request"
}
⚙️ How to Run Locally
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/Biswajeet111/ai-voice-detection.git
cd ai-voice-detection
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set API Key
Create a .env file:

env
Copy code
API_KEY=sk_test_123456789
5️⃣ Run Server
bash
Copy code
uvicorn app.main:app --reload
Open browser:

arduino
Copy code
http://127.0.0.1:8000/docs
🧪 Testing the API
The Swagger UI allows easy testing:

Paste Base64 MP3 audio

Select language

Provide API key

Execute request

📦 Project Structure
bash
Copy code
ai-voice-detection/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── schemas.py
│   ├── audio_utils.py
│   └── detector.py
│
├── models/
├── requirements.txt
├── README.md
└── .env
⚠️ Rules & Compliance
❌ No hard-coded results

❌ No misuse of data

❌ No audio modification

✅ Ethical AI usage

✅ Transparent explanations

✅ Secure API access

🏁 Conclusion
This project provides a reliable and scalable solution for detecting AI-generated voices across multiple Indian languages.
It is designed with accuracy, security, and explainability in mind, making it suitable for real-world deployment and evaluation.

👨‍💻 Author
Biswajeet Kumar
Hackathon Project – AI Voice Detection



