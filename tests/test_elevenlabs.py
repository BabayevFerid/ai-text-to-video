import unittest
from backend.services.elevenlabs_service import ElevenLabsService

class TestElevenLabsService(unittest.TestCase):

    def setUp(self):
        self.service = ElevenLabsService()

    def test_text_to_speech_creates_file(self):
        output_file = "test_narration.mp3"
        result = self.service.text_to_speech("Test səs", output_file)
        self.assertEqual(result, output_file)
        with open(output_file, "rb") as f:
            content = f.read()
        self.assertTrue(len(content) > 0)

if __name__ == "__main__":
    unittest.main()
