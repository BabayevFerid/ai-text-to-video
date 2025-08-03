import unittest
import os
from backend.services.video_service import create_video_from_image_audio

class TestVideoService(unittest.TestCase):

    def test_create_video(self):
        # Test üçün kiçik dummy image və audio faylları olmalıdır.
        # Burada manual şəkildə yerləşdirilmiş olmalıdır test_image.png və test_audio.mp3
        image_path = "tests/test_image.png"
        audio_path = "tests/test_audio.mp3"
        output_path = "tests/test_output.mp4"

        # Fayllar yoxdursa test skip olunsun
        if not (os.path.exists(image_path) and os.path.exists(audio_path)):
            self.skipTest("Test üçün image və audio faylları yoxdur.")

        result = create_video_from_image_audio(image_path, audio_path, output_path)
        self.assertTrue(os.path.exists(result))
        self.assertTrue(result.endswith(".mp4"))

if __name__ == "__main__":
    unittest.main()
