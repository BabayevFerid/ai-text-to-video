import unittest
from backend.services.openai_service import OpenAIService

class TestOpenAIService(unittest.TestCase):

    def setUp(self):
        self.service = OpenAIService()

    def test_generate_image_returns_url(self):
        url = self.service.generate_image("A beautiful sunset over mountains")
        self.assertTrue(url.startswith("http"))

if __name__ == "__main__":
    unittest.main()
