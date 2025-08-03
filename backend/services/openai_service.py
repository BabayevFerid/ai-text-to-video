import openai
from backend.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class OpenAIService:
    """
    OpenAI GPT-4 və DALL·E interfeysi.
    """

    def generate_image(self, prompt: str, size: str = "1024x1024") -> str:
        """
        DALL·E API vasitəsilə şəkil yaradır və URL qaytarır.
        """
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size
        )
        image_url = response['data'][0]['url']
        return image_url

    def split_text_to_scenes(self, text: str) -> str:
        """
        Uzun mətni səhnələrə bölmək üçün GPT-4-dən istifadə edir.
        """
        prompt = f"""
        Please split the following text into scenes with titles and short descriptions.

        Text:
        {text}

        Format:
        1. Scene Title: ...
           Description: ...
        2. Scene Title: ...
           Description: ...
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
