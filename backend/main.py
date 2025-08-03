from services.elevenlabs_service import ElevenLabsService
from services.openai_service import OpenAIService
from services.video_service import create_video_from_image_audio
from utils.downloader import download_file

def main_process(user_text: str) -> str:
    """
    İstifadəçinin daxil etdiyi mətni qəbul edir,
    səsləndirir, şəkil yaradır və videoya montaj edir.
    """
    openai_service = OpenAIService()
    elevenlabs_service = ElevenLabsService()

    print("Səs yaradılır...")
    audio_file = elevenlabs_service.text_to_speech(user_text)

    print("Şəkil yaradılır...")
    image_url = openai_service.generate_image(user_text)
    image_file = download_file(image_url, "image.png")

    print("Video yaradılır...")
    video_file = create_video_from_image_audio(image_file, audio_file)

    print(f"Video hazırdır: {video_file}")
    return video_file

if __name__ == "__main__":
    text = input("Nə yaratmaq istəyirsiniz? Yazın: ")
    main_process(text)
