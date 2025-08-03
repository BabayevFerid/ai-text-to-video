import os
from dotenv import load_dotenv

load_dotenv()  # .env faylını yükləyir

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not OPENAI_API_KEY or not ELEVENLABS_API_KEY:
    raise EnvironmentError("API açarları .env faylında təyin edilməyib!")
