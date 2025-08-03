from services.elevenlabs_service import ElevenLabsService
from services.openai_service import OpenAIService
from services.video_service import create_video_from_image_audio
from utils.downloader import download_file

def main():
    user_input = input("Nə yaratmaq istəyirsiniz? Yazın: ")

    # İnterfeyslər
    openai_service = OpenAIService()
    elevenlabs_service = ElevenLabsService()

    # 1. Səs yaratmaq
    audio_file = elevenlabs_service.text_to_speech(user_input)

    # 2. Şəkil yaratmaq
    image_url = openai_service.generate_image(user_input)
    image_file = download_file(image_url, "image.png")

    # 3. Video yaratmaq
    video_file = create_video_from_image_audio(image_file, audio_file)

    print(f"\nVideo hazırdır: {video_file}")

if __name__ == "__main__":
    main()
