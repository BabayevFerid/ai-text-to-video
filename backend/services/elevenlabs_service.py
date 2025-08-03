import requests
from backend.config import ELEVENLABS_API_KEY

class ElevenLabsService:
    def __init__(self, voice_id="EXAVITQu4vr4xnSDxMaL"):
        self.voice_id = voice_id
        self.api_key = ELEVENLABS_API_KEY
        self.tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

    def text_to_speech(self, text: str, output_file: str = "narration.mp3") -> str:
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.7
            }
        }
        response = requests.post(self.tts_url, headers=headers, json=payload)
        if response.status_code != 200:
            raise RuntimeError(f"ElevenLabs API Error: {response.text}")

        with open(output_file, "wb") as f:
            f.write(response.content)
        return output_file
